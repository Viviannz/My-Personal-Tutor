# Personal Learning Tutor 🎓

An AI-powered personal tutor built with **OpenAI Agent Builder** that helps you learn any topic quickly and practically. Features advanced guardrails for safety and a clean web interface.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

## ✨ Features

- **🎯 80/20 Learning Approach**: Focuses on the most important 20% that gives you 80% of results
- **📋 4-Hour Learning Plans**: Creates actionable plans split into manageable sections
- **💬 Conversational Interface**: Natural chat with frequent comprehension checks
- **🔄 Adaptive Teaching**: Adjusts explanations based on your understanding
- **🛡️ Advanced Guardrails**: Built-in safety features including:
  - PII Detection & Anonymization
  - Content Moderation
  - Jailbreak Prevention
  - Prompt Injection Detection
  - URL Filtering
- **🎨 Clean Web UI**: Professional, easy-to-use interface
- **🔑 User API Keys**: Users provide their own OpenAI API keys

## 🚀 Quick Start

### Option 1: Deploy to Railway (Recommended)

1. **Click the "Deploy on Railway" button above**
2. **Connect your GitHub account** and select this repository
3. **Deploy** - Railway will automatically build and deploy
4. **Get your URL** from Railway settings → Networking → Generate Domain
5. **Share the URL** - users enter their own API keys!

### Option 2: Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/Viviannz/My-Personal-Tutor.git
   cd My-Personal-Tutor
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment (optional)**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

4. **Build and run**
   ```bash
   npm run build
   npm start
   ```

5. **Open your browser** to `http://localhost:3000`

### Development Mode

```bash
npm run dev
```

This uses `tsx` for faster TypeScript development without building.

## 🔑 Getting an OpenAI API Key

Users need their own OpenAI API keys:

1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Enter it in the web interface

**Cost**: Pay-as-you-go. A typical learning session costs $0.10-0.50 depending on length.

## 📖 How to Use

1. **Visit the web interface** (your deployed URL or localhost:3000)
2. **Enter your OpenAI API key** in the input field
3. **Start chatting** with your personal tutor
4. **Tell it what you want to learn** - anything from Python to photography!
5. **Follow the structured learning plan** it creates for you

## 🎓 How It Works

The tutor follows a proven 6-step learning approach:

1. **Clarifies Topic & Scope**: Confirms what you want to learn and sets realistic goals for today
2. **Applies 80/20 Rule**: Identifies 3-5 core foundations that matter most
3. **Explains Simply**: Uses everyday comparisons and examples
4. **Builds Learning Plan**: Creates a 4-hour plan split into manageable sections
5. **Teaches Immediately**: Starts teaching right away with frequent check-ins
6. **Adapts On-The-Go**: Offers quizzes, practice tasks, or different explanations as needed

## 🛡️ Built-in Safety Features (Guardrails)

This tutor includes enterprise-grade safety guardrails:

- **PII Detection**: Automatically detects and anonymizes credit cards, SSNs, passport numbers, etc.
- **Content Moderation**: Blocks harmful content categories
- **Jailbreak Prevention**: Prevents attempts to bypass safety measures
- **Prompt Injection Detection**: Protects against malicious prompts
- **URL Filtering**: Only allows safe HTTPS URLs
- **Custom Checks**: Ensures conversations stay focused on learning

## 📁 Project Structure

```
My-Personal-Tutor/
├── src/
│   ├── workflow.ts      # OpenAI Agent Builder workflow with guardrails
│   └── server.ts        # Express.js web server
├── public/
│   └── index.html       # Clean web interface
├── package.json         # Node.js dependencies
├── tsconfig.json        # TypeScript configuration
├── railway.json         # Railway deployment config
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Technical Details

### Built With

- **OpenAI Agent Builder SDK** (`@openai/agents`)
- **OpenAI Guardrails SDK** (`@openai/guardrails`)
- **GPT-5.2** model with reasoning capabilities
- **Express.js** for the web server
- **TypeScript** for type safety
- **Web Search Tool** for real-time information

### Workflow ID

This agent is registered with OpenAI Agent Builder:
```
workflow_id: wf_6958981e6614819081ee61d758a96d730d95d548d7a74d9b
```

### API Endpoints

**POST /api/chat**
```json
{
  "message": "I want to learn Python",
  "apiKey": "sk-..."
}
```

Response:
```json
{
  "success": true,
  "response": "Great choice! What is your learning goal..."
}
```

**GET /health**
Health check endpoint

## 🚂 Railway Deployment Guide

### Step-by-Step

1. **Push your code to GitHub** (already done!)
2. **Go to [railway.app](https://railway.app)**
3. **Sign up/Login with GitHub**
4. **Click "New Project" → "Deploy from GitHub repo"**
5. **Select `My-Personal-Tutor` repository**
6. **Railway auto-detects Node.js and builds**
7. **Click "Deploy"**
8. **Generate Domain**: Settings → Networking → Generate Domain

### Important Notes

- **No environment variables needed!** Users enter API keys in the UI
- Railway provides **500 hours/month free** on trial
- App auto-sleeps when inactive, wakes instantly
- Build time: ~2-3 minutes

## 💰 Cost Estimates

### Hosting (Railway)
- **Free tier**: 500 hours/month, $5 credit
- **After free tier**: ~$5-10/month for light usage

### API Usage (Per User Session)
- **GPT-5.2**: ~$0.10-0.50 per hour of tutoring
- Users pay for their own API usage
- Your hosting costs stay minimal!

## 🔒 Security & Privacy

- **API keys are never stored** - users enter them each session
- **Keys are only in memory** during the request
- **PII is automatically anonymized** before processing
- **Guardrails run on every message** for safety
- **No conversation data saved** on the server

## 🐛 Troubleshooting

**"OpenAI API key is required"**
- Make sure users enter their API key in the web interface

**Build fails on Railway**
- Check that `package.json` and `tsconfig.json` exist
- Ensure Node.js version is 18+ in `package.json` engines

**"Module not found" errors**
- Run `npm install` to install dependencies
- Check that `@openai/agents` and `@openai/guardrails` are installed

**Agent not responding**
- Verify OpenAI API key is valid
- Check API key has sufficient credits
- Look at Railway logs for error details

## 📚 Example Learning Topics

This tutor can help with virtually any topic:

- **Programming**: Python, JavaScript, Web Development, TypeScript
- **Languages**: Spanish, French, Mandarin, English
- **Skills**: Photography, Drawing, Music Theory, Writing
- **Professional**: Excel, Public Speaking, Project Management
- **Academic**: Math, Physics, History, Biology
- **Hobbies**: Cooking, Gardening, Chess, Fitness

**The possibilities are endless!**

## 🛠️ Development

### Build TypeScript
```bash
npm run build
```

### Watch Mode
```bash
npm run watch
```

### Development Server
```bash
npm run dev
```

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Submit pull requests
- Share your learning success stories!

## 📄 License

MIT License - feel free to use this for personal or commercial projects.

## 🙏 Acknowledgments

- Built with [OpenAI Agent Builder](https://platform.openai.com/docs/guides/agent-builder)
- Powered by [GPT-5.2](https://openai.com/) with reasoning capabilities
- Inspired by effective learning principles and the 80/20 rule

---

**Happy Learning!** 🚀

Start your learning journey today with an AI tutor that adapts to your needs, keeps you safe, and helps you take action.

Questions? Open an issue on GitHub!
