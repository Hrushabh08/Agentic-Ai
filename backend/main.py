import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.agents.chat_agent import chat_with_pharmacy
from backend.agents.inventory_agent import check_refill_alerts

app = FastAPI(title="Agentic Pharmacy API")

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(user_message: UserMessage):
    response = chat_with_pharmacy(user_message.message)
    return {"response": response}

@app.get("/alerts")
def alerts_endpoint():
    alerts = check_refill_alerts(threshold=10)
    return {"alerts": alerts}
