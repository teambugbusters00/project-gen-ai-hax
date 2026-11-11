# GenAI Document Summarizer

Provider-agnostic summarization endpoint using an OpenAI-compatible chat completions API.

```bash
pip install -r requirements.txt
export AI_API_KEY=your_key
export AI_MODEL=gpt-4o-mini
uvicorn app:app --reload
```

Optional: set AI_BASE_URL for a compatible provider. Never commit API keys. Treat summaries as drafts and verify facts against the source.

## Live deployment

- **Frontend:** https://project-gen-ai-hax-frontend-vijayjangids-projects.vercel.app
- **Backend API:** https://genai-document-summarizer-api.onrender.com
- **API docs:** https://genai-document-summarizer-api.onrender.com/docs

> Deployment is an MVP. Configure required secrets (if any), add authentication, and use durable database storage before production use.
