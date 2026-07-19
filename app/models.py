from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base #this base thingy and wrote column instead of Column
from datetime import datetime#dont know why redlinesJ

class User(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key = True, index = True)
    
    name = Column(String, unique = False )
    
    role = Column(String) 
    
    email = Column(String, unique = True)
    
    
class Agent(Base):
    __tablename__ = "agent"

    id = Column(Integer, primary_key = True, index = True)  
    
    hostname = Column(String)
    
    operating_system = Column(String)
    
    api_key = Column(String)
    
    created_at = Column(DateTime, default= datetime.utcnow)
    
    status = Column(String, default= "OFFLINE")
    
    last_seen = Column(DateTime, nullable= True)
    
    telemetries = relationship("Telemetry", back_populates="agent")
    
    
class Telemetry(Base):
    __tablename__ = "telemetry"
    
    id = Column(Integer, primary_key=True, index= True)
    
    cpu = Column(Float) #why Float and not float?
    
    ram = Column(Float)
    
    disk = Column(Float)
    
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    agent_id = Column(Integer, ForeignKey("agent.id"))
    
    agent = relationship("Agent", back_populates="telemetries")
    
    
class Incident(Base):
    
    __tablename__ = "incidents"
    
    id = Column(Integer, primary_key= True, index = True)
    
    Incidenttype = (String)
    
    severity = Column(String)
    
    description = Column(String)
    
    status = Column(String , default= "OPEN")
    
    created_at = Column(DateTime, default= datetime.utcnow)
    
    agent_id = Column(Integer, ForeignKey("agent.id")) #why?
    
    ##relationship bhangbhosda
    
class Rule(Base):
    __tablename__ = "rule"
    
    id = Column(Integer, primary_key= True, index = True)
    
    metric = Column(String)
    
    threshold = Column(Float)
    
    severity = Column(String)
    
    enabled = Column(bool, default= True)
    
    
    
    
    
    
    