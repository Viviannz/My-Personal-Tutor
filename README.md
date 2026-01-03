# Personal Learning Tutor 🎓

An AI-powered personal tutor that helps you learn any topic quickly and practically. Features a clean web interface with support for both OpenAI and Anthropic AI models.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

## ✨ Features

- **🎯 80/20 Approach**: Focuses on the most important 20% that gives you 80% of results
- **📋 4-Hour Learning Plans**: Creates actionable plans split into manageable sections
- **💬 Conversational Interface**: Natural chat with frequent comprehension checks
- **🔄 Adaptive Learning**: Adjusts explanations based on your understanding
- **🎨 Clean UI**: Professional, easy-to-use web interface (no purple!)
- **🔑 Multi-Provider**: Choose between OpenAI or Anthropic (you bring your own API key)

## 🌟 What Makes This Tutor Special

- Starts from zero unless you say otherwise
- Uses plain language suitable for 8th grade reading level
- Provides everyday examples and comparisons
- Keeps scope narrow and practical for same-day progress
- Warm, calm, and supportive tone throughout

## 🚀 Quick Start

### Option 1: Deploy to Railway (Recommended)

1. **Click the "Deploy on Railway" button above**
2. **Connect your GitHub account** and select this repository
3. **No environment variables needed!** Users enter their own API keys in the web interface
4. **Deploy** and get your live URL

That's it! Your tutor will be live and ready to use.

### Option 2: Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/Viviannz/My-Personal-Tutor.git
   cd My-Personal-Tutor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web app**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

5. **Enter your API key** in the sidebar and start learning!

## 🔑 Getting API Keys

Users need their own API keys (not stored on the server):

- **OpenAI**: Get a key at [platform.openai.com](https://platform.openai.com/api-keys)
- **Anthropic**: Get a key at [console.anthropic.com](https://console.anthropic.com/settings/keys)

Both providers offer pay-as-you-go pricing. A typical learning session costs $0.10-0.50.

## 📖 How to Use

1. **Choose your AI provider** (OpenAI or Anthropic) in the sidebar
2. **Enter your API key** (kept secure, never stored)
3. **Click "Start Learning Session"**
4. **Tell the tutor what you want to learn**
5. **Follow the step-by-step guidance**
6. **Take action today!**

## 🎓 How It Works

The tutor follows a structured 6-step approach:

1. **Clarifies Topic & Scope**: Confirms what you want to learn and sets realistic goals for today
2. **Applies 80/20 Rule**: Identifies 3-5 core foundations that matter most
3. **Explains Simply**: Uses everyday comparisons and examples
4. **Builds Learning Plan**: Creates a 4-hour plan split into manageable sections
5. **Teaches Immediately**: Starts teaching right away with frequent check-ins
6. **Adapts On-The-Go**: Offers quizzes, practice tasks, or different explanations as needed

## 📁 Project Structure

```
My-Personal-Tutor/
├── app.py              # Streamlit web interface
├── tutor_agent.py      # Core tutor logic (multi-provider)
├── requirements.txt    # Python dependencies
├── Procfile           # Railway deployment config
├── railway.json       # Railway configuration
├── .streamlit/
│   └── config.toml    # Streamlit theme (clean, not purple!)
├── .env.example       # Example environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🛠️ Advanced Usage

### CLI Mode

For command-line enthusiasts:

```bash
python tutor_agent.py
```

You'll be prompted to choose a provider and enter your API key.

### Customization

Edit `TUTOR_SYSTEM_PROMPT` in `tutor_agent.py` to customize:
- Teaching style and tone
- Learning structure and steps
- How the tutor adapts to your needs

### Supported Models

**OpenAI:**
- `gpt-4o` (default, recommended)
- `gpt-4o-mini` (faster, cheaper)
- `gpt-4-turbo`

**Anthropic:**
- `claude-3-5-sonnet-20241022` (default, recommended)
- `claude-3-opus-20240229` (most capable)
- `claude-3-haiku-20240307` (fastest, cheapest)

## 🚂 Railway Deployment Guide

### Step-by-Step Deployment

1. **Push your code to GitHub**
2. **Go to [railway.app](https://railway.app)**
3. **Sign up/Login with GitHub**
4. **Click "New Project" → "Deploy from GitHub repo"**
5. **Select `My-Personal-Tutor` repository**
6. **Railway auto-detects the configuration**
7. **Click "Deploy"**
8. **Get your public URL** (Settings → Generate Domain)

### Important Notes

- **No environment variables needed!** Users enter API keys in the UI
- Railway provides **500 hours/month free** on the trial plan
- App automatically sleeps when inactive
- Wakes up instantly when accessed

## 💰 Cost Estimates

### Hosting (Railway)
- **Free tier**: 500 hours/month, $5 credit
- **After free tier**: ~$5-10/month for light usage

### AI API Usage (Per User Session)
- **OpenAI GPT-4o**: $0.10-0.50 per hour of tutoring
- **Anthropic Claude 3.5 Sonnet**: $0.10-0.50 per hour of tutoring
- **Budget options** (GPT-4o-mini, Claude Haiku): $0.02-0.10 per hour

Users pay for their own API usage, so your hosting costs are minimal!

## 🎨 UI Customization

The interface uses a professional blue/gray color scheme. To customize:

1. Edit `.streamlit/config.toml` for theme colors
2. Modify CSS in `app.py` for detailed styling
3. Current theme: Clean, professional, **definitely not purple!**

## 🔒 Security & Privacy

- **API keys are never stored** - users enter them each session
- **No conversation data is saved** on the server
- **All AI requests go directly** from user's browser to AI provider
- **Session data is temporary** and cleared on reset

## 🐛 Troubleshooting

**"Please enter your API key first!"**
- Make sure you've entered a valid API key in the sidebar

**"Error: ANTHROPIC_API_KEY not found"**
- You're in CLI mode. Enter the key when prompted, or create a `.env` file

**"Connection error"**
- Check your internet connection
- Verify your API key is valid and has credits
- Check provider status page

**App won't deploy to Railway**
- Ensure `Procfile` and `railway.json` are in the root directory
- Check Railway build logs for specific errors

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Submit pull requests
- Share your learning success stories!

## 📄 License

MIT License - feel free to use this for personal or commercial projects.

## 🙏 Acknowledgments

- Built with [Anthropic's Claude](https://www.anthropic.com/) and [OpenAI's GPT](https://openai.com/)
- Web interface powered by [Streamlit](https://streamlit.io/)
- Inspired by effective learning principles and the 80/20 rule

---

## 📚 Example Learning Topics

This tutor can help with virtually any topic:

- **Programming**: Python, JavaScript, Web Development, Data Science
- **Languages**: Spanish, French, Mandarin, English
- **Skills**: Photography, Drawing, Music Theory, Writing
- **Professional**: Excel, Public Speaking, Project Management
- **Academic**: Math, Physics, History, Biology
- **Hobbies**: Cooking, Gardening, Chess, Fitness

**The possibilities are endless!**

---

**Happy Learning!** 🚀

Start your learning journey today with a personal AI tutor that adapts to your needs.

Questions? Open an issue on GitHub!
