from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Agent, Telemetry, Incident
from schemas import AgentRetrieval, Agentcreate, AgentBase, AgentUpdate, agentregistration,incidentresponce,createincident, agentresponse,heartbeatresponse, telemetrycreate, telemeryresponse
import uuid, secrets
from fastapi.security import APIKeyHeader

router = APIRouter(prefix="/telemetry",
                   tags=["Telemetry"])


api_keyheader = APIKeyHeader(
    name= "Authorization"
)
router = APIRouter(
    prefix="/agents",
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
def getagents(db : Session = Depends(get_db)):
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
def registering(agentinput: agentregistration, db : Session = Depends(get_db)):
    
    agent_id = f"AGT - {uuid.uuid4().hex[:8].upper()}"
    
    api_key = secrets.token_hex(32)
    
    db_agent = Agent(
        agent_id = agent_id,
        hostname = agent.hostname,
        operating_system = agent.operating_system
        api_key = api_key
        
        db.add(db_agent)
        db.commit()
        db.refresh(db_agent)
        return db_agent
    )
    
def authenticate (api_key : str = Depends(api_keyheader), db : Session = Depends(get_db)):
    
    api_key = api_key.replace("Bearer ", "")
    
    agent = db.query(Agent).filter(Agent.api_key == api_key).first() #still search it once agian
    
    if agent is None:
        raise HTTPException(status_code=401, detail = "Invalid api key")
    
    return agent

@router.post("/", response_model=telemeryresponse)
def create_telemetery(telemetry : telemetrycreate, agent : Agent = Depends(authenticate), db : Session = Depends(get_db)):
    db_telemetry = Telemetry(
        cpu = telemetry.cpu,
        ram = telemetry.ram,
        disk = telemetry.disk,
        agent_id = agent.id
    )
    
    db.add(db_telemetry)
    db.commit()
    db.refresh(db_telemetry)
    
    return db_telemetry

@router.post("/heartbeats", response_model= heartbeatresponse )
def heartbeat(agent : Agent = Depends(authenticate), db : Session = Depends(get_db)):
    agent.status = "ONLINE"
    agent.last_seen = datetime.utcnow()
    db.commit()
    db.refresh(agent)
    return agent

@router.post("/incidents", response_model= incidentresponce)
def create_incident(incident : createincident, agent : Agent = Depends(authenticate), db : Session = Depends(get_db) ):
    db_incident = Incident(
        Incidenttype = incident.inciedent_type
        severity = incident.severity
        description = incident.descryption
        agent_id = agent.id
        )