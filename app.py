"""Run: pip install fastapi uvicorn httpx; uvicorn app:app --reload"""
import os,httpx
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app=FastAPI(title="GenAI Document Summarizer")
class Request(BaseModel):text:str=Field(min_length=80,max_length=30000);style:str="bullet points"
@app.post("/summarize")
async def summarize(x:Request):
 key=os.getenv("AI_API_KEY");base=os.getenv("AI_BASE_URL","https://api.openai.com/v1");model=os.getenv("AI_MODEL","gpt-4o-mini")
 if not key:raise HTTPException(503,"Set AI_API_KEY before using model inference.")
 payload={"model":model,"messages":[{"role":"system","content":"Summarize faithfully. Do not add facts not present in the source."},{"role":"user","content":f"Summarize as {x.style}:\n{x.text}"}],"temperature":0.2}
 async with httpx.AsyncClient(timeout=60) as client:
  r=await client.post(base.rstrip("/")+"/chat/completions",headers={"Authorization":f"Bearer {key}"},json=payload)
 if r.is_error:raise HTTPException(r.status_code,"Model provider request failed.")
 return {"summary":r.json()["choices"][0]["message"]["content"]}