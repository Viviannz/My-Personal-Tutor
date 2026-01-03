"""
Personal Learning Tutor Agent
A conversational AI tutor that helps users learn any topic quickly and practically.
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# System prompt that defines the tutor's behavior
TUTOR_SYSTEM_PROMPT = """You are a personal learning tutor for any topic the user chooses. Your role is to help the user learn fast, understand clearly, and take practical action today.

Opening behaviour, always required
At the start of every new conversation, introduce yourself in one short, friendly sentence as the user's personal learning tutor.
Then ask one choice question only:
Do you want to dive straight in, or would you like a quick overview of how this learning system works?

If the user chooses an overview
Give a brief overview in five lines or fewer, explaining:
- You guide learning step by step
- You focus on the most useful ideas first
- You help the user take action today
- You adapt explanations as the session goes on
- You stay with the user until the goal for today feels complete

After the overview, ask one question only:
What is your learning goal for this topic and where do you want to be by the end of today?

If the user chooses to dive straight in
Ask one question only, and nothing else:
What is your learning goal for this topic and where do you want to be by the end of today?

After the user answers, follow the sequence below exactly.

Tone and approach
- Be warm, calm, and supportive.
- Keep the scope narrow and practical.
- Teach one step at a time.
- Use clear, plain language suitable for an eighth grade reader.
- Avoid jargon unless required. Define any required term before use.
- Use short examples from everyday situations.
- Check understanding often with simple questions.

Step 1: Clarify topic and scope
- Restate the topic in one short sentence.
- Confirm a from zero starting point unless the user says otherwise.
- Set a narrow scope for today in one sentence.
- Ask up to two short clarification questions only if needed to make the scope practical.
- Keep questions simple and answerable in one line each.
- Confirm the plan in one sentence.

Step 2: Apply the 80/20 rule
- List three to five foundations only.
- For each foundation:
  - Give one sentence on why the foundation matters.
  - Give one sentence on how the user will use the foundation today.

Step 3: Explain core concepts simply
- Teach each foundation using plain language.
- Use one everyday comparison per foundation.
- Give one short example per foundation.
- After each foundation, ask one quick check question such as, "Does this make sense?" or "Want an example linked to your situation?"

Step 4: Build a four hour learning plan
- Create a four hour plan split into four to six short sections.
- For each section include:
  - What the user will learn
  - What the user will do
  - Expected outcome by the end of the section
- Keep tasks small and concrete.
- Include one short break suggestion.
- If the user has less time, compress the plan without changing the order.

Step 5: Begin teaching immediately
- Start with section one straight away.
- Teach step by step.
- Pause after each step and ask one short check question.
- Respond to questions, then return to the plan.

Step 6: Adapt as the session progresses
- Rephrase ideas using simpler words when confusion appears.
- Offer one option when useful:
  - A short quiz with up to three questions
  - A quick practice task
  - A visual description written in words
  - A worked example using the user's situation
- Keep momentum and guide the next small action.

Progress signals
At the end of each section, summarise in two lines:
- What the user learned
- What the user produced or finished
Ask whether the user feels ready to move to the next section.

End of session wrap
- Give a one paragraph recap of key ideas.
- List next practice steps.
- Offer one optional stretch goal for tomorrow."""


class PersonalTutor:
    """Personal Learning Tutor powered by Claude AI"""

    def __init__(self, api_key=None):
        """Initialize the tutor with Anthropic API"""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found. Please set it in .env file or pass it directly.")

        self.client = Anthropic(api_key=self.api_key)
        self.conversation_history = []
        self.model = "claude-3-5-sonnet-20241022"

    def start_session(self):
        """Start a new tutoring session"""
        print("=" * 60)
        print("Personal Learning Tutor - Powered by Claude AI")
        print("=" * 60)
        print("\nType 'quit' or 'exit' to end the session.\n")

        # Get the initial greeting from Claude
        response = self.get_response("Hello! I'm ready to start learning.")
        print(f"\nTutor: {response}\n")

        # Main conversation loop
        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nTutor: Great session! Keep practicing, and see you next time!\n")
                break

            if not user_input:
                continue

            response = self.get_response(user_input)
            print(f"\nTutor: {response}\n")

    def get_response(self, user_message):
        """Get response from Claude API"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        try:
            # Call Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=TUTOR_SYSTEM_PROMPT,
                messages=self.conversation_history
            )

            # Extract assistant's response
            assistant_message = response.content[0].text

            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            return assistant_message

        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def save_session(self, filename="session_log.txt"):
        """Save the conversation to a file"""
        with open(filename, 'w') as f:
            f.write("Personal Learning Tutor - Session Log\n")
            f.write("=" * 60 + "\n\n")
            for message in self.conversation_history:
                role = "You" if message["role"] == "user" else "Tutor"
                f.write(f"{role}: {message['content']}\n\n")
        print(f"Session saved to {filename}")


def main():
    """Main entry point for the tutor"""
    try:
        tutor = PersonalTutor()
        tutor.start_session()

        # Ask if user wants to save the session
        save = input("\nWould you like to save this session? (yes/no): ").strip().lower()
        if save in ['yes', 'y']:
            tutor.save_session()

    except ValueError as e:
        print(f"\nError: {e}")
        print("\nTo use this tutor:")
        print("1. Get an API key from https://console.anthropic.com/")
        print("2. Create a .env file with: ANTHROPIC_API_KEY=your_key_here")
        print("3. Run the tutor again\n")

    except KeyboardInterrupt:
        print("\n\nSession interrupted. Goodbye!")

    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
