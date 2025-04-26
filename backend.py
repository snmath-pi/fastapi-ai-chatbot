# Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
    
# Step2: Setup AI agent from frontend request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAME = ["llama3-70b-8192", "mixtral-8x7b-3278", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title="Langgraph AI Agent")

@app.post('/chat')
async def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with chatbot using langgraph and search tool
    It dynmically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAME:
        return {"message": "Error! invalid model name. Kindly select a relevant AI Model"}
    
    """
    Create AI Agent and get response from it
    """
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)  
    return {"message": "success", "response": response}
 
# Step3: Run app & explore swagger ui docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.01", port=8083)