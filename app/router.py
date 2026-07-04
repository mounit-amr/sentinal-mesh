from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Agent
from schemas import AgentRetrieval, Agentcreate, AgentBase, AgentUpdate

router = APIRouter(
    prefix="/agents" 
    tags=["Agents"]
)

@router.post("/", response_model= AgentRetrieval)
def createagent(agent: Agentcreate, db : Session = Depends(get_db)):
    db_agent = Agent(hostname= agent.hostname , operating_system = agent.operating_system)
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent
    
@router.get("/Agents", response_model= AgentRetrieval)
def get_agents(db : Session = Depends(get_db)):
    agents = db.query(Agent).all()
    return agents

@router.put("/update", response_model= AgentRetrieval)
def update_agent(id : int, update_agent : AgentUpdate, db : Session = Depends(get_db)):
    
    agent = db.query(Agent).filter(Agent.id == id).first()
    
    if update_agent.hostname is not None:
        agent.hostname =update_agent.hostname 
        
    db.commit()
    db.refresh(agent)
    
    return agent
    