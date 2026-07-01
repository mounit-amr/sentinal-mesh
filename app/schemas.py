from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AgentBase(BaseModel):
    hostname : str
    ip_address : str
    operating_system : str
    
class Agentcreate(AgentBase):
    pass

class AgentUpdate(BaseModel):
    hostname : Optional[str] = None
    ip_address : Optional[str] = None
    operating_system : Optional[str] = None
    status : Optional[str] = None
    
class AgentRetrieval(BaseModel):
    id : int
    hostname : str
    ip_address : str
    operating_system : str
    status : str
    lastseen : Optional[datetime] = None
    created_at : datetime
    