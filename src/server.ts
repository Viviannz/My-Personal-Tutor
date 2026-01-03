import express from 'express';
import { runWorkflow } from './workflow.js';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

// API endpoint to run the tutor workflow
app.post('/api/chat', async (req, res) => {
  try {
    const { message, apiKey } = req.body;

    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // Set API key from user input if provided
    if (apiKey) {
      process.env.OPENAI_API_KEY = apiKey;
    }

    if (!process.env.OPENAI_API_KEY) {
      return res.status(400).json({
        error: 'OpenAI API key is required. Please provide it in the request or set OPENAI_API_KEY environment variable.'
      });
    }

    const result = await runWorkflow({ input_as_text: message });

    res.json({
      success: true,
      response: result.output_text || result
    });

  } catch (error: any) {
    console.error('Error running workflow:', error);
    res.status(500).json({
      error: 'Failed to process your request',
      details: error.message
    });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'healthy', service: 'My Personal Tutor' });
});

// Start server
app.listen(PORT, () => {
  console.log(`🎓 Personal Tutor server running on port ${PORT}`);
  console.log(`📝 API endpoint: http://localhost:${PORT}/api/chat`);
  console.log(`🌐 Web interface: http://localhost:${PORT}`);
});
