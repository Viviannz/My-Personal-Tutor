import { webSearchTool, Agent, AgentInputItem, Runner, withTrace } from "@openai/agents";
import { OpenAI } from "openai";
import { runGuardrails } from "@openai/guardrails";


// Tool definitions
const webSearchPreview = webSearchTool({
  userLocation: {
    type: "approximate",
    country: undefined,
    region: undefined,
    city: undefined,
    timezone: undefined
  },
  searchContextSize: "medium"
})

// Shared client for guardrails and file search
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Guardrails definitions
const guardrailsConfig = {
  guardrails: [
    { name: "Contains PII", config: { block: false, detect_encoded_pii: true, entities: ["CREDIT_CARD", "US_BANK_NUMBER", "US_PASSPORT", "US_SSN"] } },
    { name: "Moderation", config: { categories: ["sexual/minors", "hate/threatening", "harassment/threatening", "self-harm/instructions", "violence/graphic", "illicit/violent"] } },
    { name: "Jailbreak", config: { model: "gpt-4.1-mini", confidence_threshold: 0.7 } },
    { name: "URL Filter", config: { url_allow_list: [], allowed_schemes: ["https"], block_userinfo: true, allow_subdomains: false } },
    { name: "Prompt Injection Detection", config: { model: "gpt-4.1-mini", confidence_threshold: 0.7 } },
    { name: "Custom Prompt Check", config: { system_prompt_details: "You are a customer support assistant. Raise the guardrail if questions aren't focused on customer inquiries, product support, and service-related questions.", model: "gpt-4.1-mini", confidence_threshold: 0.7 } }
  ]
};
const context = { guardrailLlm: client };

function guardrailsHasTripwire(results: any[]): boolean {
    return (results ?? []).some((r) => r?.tripwireTriggered === true);
}

function getGuardrailSafeText(results: any[], fallbackText: string): string {
    for (const r of results ?? []) {
        if (r?.info && ("checked_text" in r.info)) {
            return r.info.checked_text ?? fallbackText;
        }
    }
    const pii = (results ?? []).find((r) => r?.info && "anonymized_text" in r.info);
    return pii?.info?.anonymized_text ?? fallbackText;
}

async function scrubConversationHistory(history: any[], piiOnly: any): Promise<void> {
    for (const msg of history ?? []) {
        const content = Array.isArray(msg?.content) ? msg.content : [];
        for (const part of content) {
            if (part && typeof part === "object" && part.type === "input_text" && typeof part.text === "string") {
                const res = await runGuardrails(part.text, piiOnly, context, true);
                part.text = getGuardrailSafeText(res, part.text);
            }
        }
    }
}

async function scrubWorkflowInput(workflow: any, inputKey: string, piiOnly: any): Promise<void> {
    if (!workflow || typeof workflow !== "object") return;
    const value = workflow?.[inputKey];
    if (typeof value !== "string") return;
    const res = await runGuardrails(value, piiOnly, context, true);
    workflow[inputKey] = getGuardrailSafeText(res, value);
}

async function runAndApplyGuardrails(inputText: string, config: any, history: any[], workflow: any) {
    const guardrails = Array.isArray(config?.guardrails) ? config.guardrails : [];
    const results = await runGuardrails(inputText, config, context, true);
    const shouldMaskPII = guardrails.find((g) => (g?.name === "Contains PII") && g?.config && g.config.block === false);
    if (shouldMaskPII) {
        const piiOnly = { guardrails: [shouldMaskPII] };
        await scrubConversationHistory(history, piiOnly);
        await scrubWorkflowInput(workflow, "input_as_text", piiOnly);
        await scrubWorkflowInput(workflow, "input_text", piiOnly);
    }
    const hasTripwire = guardrailsHasTripwire(results);
    const safeText = getGuardrailSafeText(results, inputText) ?? inputText;
    return { results, hasTripwire, safeText, failOutput: buildGuardrailFailOutput(results ?? []), passOutput: { safe_text: safeText } };
}

function buildGuardrailFailOutput(results: any[]) {
    const get = (name: string) => (results ?? []).find((r: any) => ((r?.info?.guardrail_name ?? r?.info?.guardrailName) === name));
    const pii = get("Contains PII"), mod = get("Moderation"), jb = get("Jailbreak"), hal = get("Hallucination Detection"), nsfw = get("NSFW Text"), url = get("URL Filter"), custom = get("Custom Prompt Check"), pid = get("Prompt Injection Detection"), piiCounts = Object.entries(pii?.info?.detected_entities ?? {}).filter(([, v]) => Array.isArray(v)).map(([k, v]) => k + ":" + v.length), conf = jb?.info?.confidence;
    return {
        pii: { failed: (piiCounts.length > 0) || pii?.tripwireTriggered === true, detected_counts: piiCounts },
        moderation: { failed: mod?.tripwireTriggered === true || ((mod?.info?.flagged_categories ?? []).length > 0), flagged_categories: mod?.info?.flagged_categories },
        jailbreak: { failed: jb?.tripwireTriggered === true },
        hallucination: { failed: hal?.tripwireTriggered === true, reasoning: hal?.info?.reasoning, hallucination_type: hal?.info?.hallucination_type, hallucinated_statements: hal?.info?.hallucinated_statements, verified_statements: hal?.info?.verified_statements },
        nsfw: { failed: nsfw?.tripwireTriggered === true },
        url_filter: { failed: url?.tripwireTriggered === true },
        custom_prompt_check: { failed: custom?.tripwireTriggered === true },
        prompt_injection: { failed: pid?.tripwireTriggered === true },
    };
}
const myPersonalTutor = new Agent({
  name: "My Personal Tutor",
  instructions: `You are a helpful assistant. You are a personal learning tutor for any topic the user chooses. Your role is to help the user learn fast, understand clearly, and take practical action today.
Opening behaviour, always required
At the start of every new conversation, introduce yourself in one short, friendly sentence as the user's personal learning tutor.
Then ask one choice question only:
Do you want to dive straight in, or would you like a quick overview of how this learning system works?
If the user chooses an overview
Give a brief overview in five lines or fewer, explaining
You guide learning step by step
You focus on the most useful ideas first
You help the user take action today
You adapt explanations as the session goes on
You stay with the user until the goal for today feels complete
After the overview, ask one question only:
What is your learning goal for this topic and where do you want to be by the end of today?
If the user chooses to dive straight in
Ask one question only, and nothing else:
What is your learning goal for this topic and where do you want to be by the end of today?
After the user answers, follow the sequence below exactly.
Tone and approach
Be warm, calm, and supportive.
Keep the scope narrow and practical.
Teach one step at a time.
Use clear, plain language suitable for an eighth grade reader.
Avoid jargon unless required. Define any required term before use.
Use short examples from everyday situations.
Check understanding often with simple questions.
Step 1, Clarify topic and scope
Restate the topic in one short sentence.
Confirm a from zero starting point unless the user says otherwise.
Set a narrow scope for today in one sentence.
Ask up to two short clarification questions only if needed to make the scope practical.
Keep questions simple and answerable in one line each.
Confirm the plan in one sentence.
Step 2, Apply the 80 20 rule
List three to five foundations only.
For each foundation
Give one sentence on why the foundation matters.
Give one sentence on how the user will use the foundation today.
Step 3, Explain core concepts simply
Teach each foundation using plain language.
Use one everyday comparison per foundation.
Give one short example per foundation.
After each foundation, ask one quick check question such as, Does this make sense, or, Want an example linked to your situation.
Step 4, Build a four hour learning plan
Create a four hour plan split into four to six short sections.
For each section include
What the user will learn
What the user will do
Expected outcome by the end of the section
Keep tasks small and concrete.
Include one short break suggestion.
If the user has less time, compress the plan without changing the order.
Step 5, Begin teaching immediately
Start with section one straight away.
Teach step by step.
Pause after each step and ask one short check question.
Respond to questions, then return to the plan.
Step 6, Adapt as the session progresses
Rephrase ideas using simpler words when confusion appears.
Offer one option when useful
A short quiz with up to three questions
A quick practice task
A visual description written in words
A worked example using the user's situation
Keep momentum and guide the next small action.
Progress signals
At the end of each section, summarise in two lines
What the user learned
What the user produced or finished
Ask whether the user feels ready to move to the next section.
End of session wrap
Give a one paragraph recap of key ideas.
List next practice steps.
Offer one optional stretch goal for tomorrow.`,
  model: "gpt-5.2",
  tools: [
    webSearchPreview
  ],
  modelSettings: {
    reasoning: {
      effort: "low",
      summary: "auto"
    },
    store: true
  }
});

type WorkflowInput = { input_as_text: string };


// Main code entrypoint
export const runWorkflow = async (workflow: WorkflowInput) => {
  return await withTrace("My Personal Tutor", async () => {
    const conversationHistory: AgentInputItem[] = [
      { role: "user", content: [{ type: "input_text", text: workflow.input_as_text }] }
    ];
    const runner = new Runner({
      traceMetadata: {
        __trace_source__: "agent-builder",
        workflow_id: "wf_6958981e6614819081ee61d758a96d730d95d548d7a74d9b"
      }
    });
    const guardrailsInputText = workflow.input_as_text;
    const { hasTripwire: guardrailsHasTripwire, safeText: guardrailsAnonymizedText, failOutput: guardrailsFailOutput, passOutput: guardrailsPassOutput } = await runAndApplyGuardrails(guardrailsInputText, guardrailsConfig, conversationHistory, workflow);
    const guardrailsOutput = (guardrailsHasTripwire ? guardrailsFailOutput : guardrailsPassOutput);
    if (guardrailsHasTripwire) {
      return guardrailsOutput;
    } else {
      const myPersonalTutorResultTemp = await runner.run(
        myPersonalTutor,
        [
          ...conversationHistory
        ]
      );
      conversationHistory.push(...myPersonalTutorResultTemp.newItems.map((item) => item.rawItem));

      if (!myPersonalTutorResultTemp.finalOutput) {
          throw new Error("Agent result is undefined");
      }

      const myPersonalTutorResult = {
        output_text: myPersonalTutorResultTemp.finalOutput ?? ""
      };
      return myPersonalTutorResult;
    }
  });
}
