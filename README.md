# GenAI Document Summarizer

Provider-agnostic summarization endpoint using an OpenAI-compatible chat completions API.

```bash
pip install -r requirements.txt
export AI_API_KEY=your_key
export AI_MODEL=gpt-4o-mini
uvicorn app:app --reload
```

Optional: set AI_BASE_URL for a compatible provider. Never commit API keys. Treat summaries as drafts and verify facts against the source.