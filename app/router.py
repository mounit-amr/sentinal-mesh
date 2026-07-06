from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Agent
from schemas import AgentRetrieval, Agentcreate, AgentBase, AgentUpdate, agentregistration, agentresponse
import uuid, secrets

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
    agent = db.query(Agent).all()
    return agent

@router.put("/{id}", response_model= AgentRetrieval)
def update_agent(id : int, update_agent : AgentUpdate, db : Session = Depends(get_db)):
    
    agent = db.query(Agent).filter(Agent.id == id).first()
    
    if update_agent.hostname is not None:
        agent.hostname =update_agent.hostname 
        
    if update_agent.operating_system is not None:
        agent.operating_system = update_agent.operating_system
        
    
    
        
    db.commit()
    db.refresh(agent)
    
    return agent
    
@router.delete("/{id}", response_model= AgentRetrieval)
def deleting(id : int , Session = Depends(get_db)):
    pass 

@router.post("/register", response_model= agentresponse)
def registering(agentinput: agentregistration, db : Session = Depends(get_agents)):
    
    agent_id = f"AGT - {uuid.uuid4().hex[:8].upper()}"
    
    api_key = secrets.token_hex(32)
    
    db_agent = Agent(
        agent_id = agent_id,
        hostname = agent.hostname,
        operating_system = agent.operating_system
        api_key = api_key
    )