import os
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="BEright Automation - Project 1: Personal AI Assistant", version="1.0")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {
        "status": "success", 
        "message": "BEright Automation Project 1 (Personal AI Assistant) is Live and Ready for Clients!"
    }

@app.post("/chat")
def chat_with_agent(data: PromptRequest):
    try:
        response = model.generate_content(data.prompt)
        return {
            "status": "success",
            "client_prompt": data.prompt,
            "ai_response": response.text
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("assistant_agent:app", host="127.0.0.1", port=8000, reload=True)