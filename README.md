# Personal Learning Tutor 🎓

An AI-powered personal tutor that helps you learn any topic quickly and practically. Built with Claude AI, this tutor guides you step-by-step, focuses on the most useful concepts first, and helps you take action today.

## Features

- **Adaptive Learning**: Teaches at your pace and adjusts explanations based on your understanding
- **80/20 Approach**: Focuses on the most important 20% that gives you 80% of results
- **Practical Focus**: Creates actionable 4-hour learning plans with concrete tasks
- **Conversational**: Natural chat-based interface that checks your understanding frequently
- **Session Logging**: Save your learning sessions for future reference

## What Makes This Tutor Special

- Starts from zero unless you say otherwise
- Uses plain language suitable for 8th grade reading level
- Provides everyday examples and comparisons
- Keeps scope narrow and practical for same-day progress
- Warm, calm, and supportive tone throughout

## Prerequisites

- Python 3.8 or higher
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com/))

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/Viviannz/My-Personal-Tutor.git
   cd My-Personal-Tutor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   Create a `.env` file in the project root:
   ```bash
   ANTHROPIC_API_KEY=your_api_key_here
   ```

   Or export it directly:
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

### Run the tutor

```bash
python tutor_agent.py
```

### Example Session

```
Personal Learning Tutor - Powered by Claude AI
============================================================

Type 'quit' or 'exit' to end the session.

Tutor: Hi! I'm your personal learning tutor, here to help you learn any topic
quickly and practically. Do you want to dive straight in, or would you like a
quick overview of how this learning system works?

You: I want to learn Python programming

Tutor: Great choice! What is your learning goal for Python and where do you
want to be by the end of today?

You: I want to build a simple calculator program
...
```

## How It Works

The tutor follows a structured 6-step approach:

1. **Clarifies Topic & Scope**: Confirms what you want to learn and sets realistic goals for today
2. **Applies 80/20 Rule**: Identifies 3-5 core foundations that matter most
3. **Explains Simply**: Uses everyday comparisons and examples
4. **Builds Learning Plan**: Creates a 4-hour plan split into manageable sections
5. **Teaches Immediately**: Starts teaching right away with frequent check-ins
6. **Adapts On-The-Go**: Offers quizzes, practice tasks, or different explanations as needed

## Commands

- Type your learning goals and questions naturally
- Type `quit`, `exit`, or `bye` to end the session
- At the end, you can save your session log

## Project Structure

```
My-Personal-Tutor/
├── tutor_agent.py      # Main tutor application
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Customization

You can modify the tutor's behavior by editing the `TUTOR_SYSTEM_PROMPT` in `tutor_agent.py`. The prompt defines:
- Teaching style and tone
- Learning structure and steps
- How the tutor adapts to your needs

## Troubleshooting

**Error: ANTHROPIC_API_KEY not found**
- Make sure you've created a `.env` file with your API key
- Or export the key: `export ANTHROPIC_API_KEY=your_key`

**API errors**
- Check your API key is valid at [console.anthropic.com](https://console.anthropic.com/)
- Ensure you have credits/quota available
- Check your internet connection

## Cost Considerations

This tutor uses Claude 3.5 Sonnet. Costs are approximately:
- $3 per million input tokens
- $15 per million output tokens

A typical 1-hour tutoring session might cost $0.10-0.50 depending on conversation length.

## Future Enhancements

Potential additions:
- Multiple AI backend support (OpenAI, local models)
- Web interface with Gradio or Streamlit
- Voice interaction capability
- Progress tracking across sessions
- Topic-specific templates
- Integration with learning resources (videos, articles)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use this for personal or commercial projects.

## Acknowledgments

- Built with [Anthropic's Claude AI](https://www.anthropic.com/)
- Inspired by effective learning principles and the 80/20 rule

---

**Happy Learning!** 🚀

Start your learning journey today with a personal AI tutor that adapts to your needs.
