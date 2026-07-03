from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Agent
from schemas import AgentRetrieval, Agentcreate, AgentBase

router = APIRouter(
    prefix="/agents"
    tags=["Agents"]
)

@router.post("/", response_model= AgentRetrieval)
def createagent(agent: Agentcreate, db : Session = Depends(get_db)):
    db_agent = AgentBase(hostname= )