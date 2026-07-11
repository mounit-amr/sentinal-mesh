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
    __tablename__ = "Agent"

    id = Column(Integer, primary_key = True, index = True)  
    
    hostname = Column(String)
    
    operating_system = Column(String)
    
    api_key = Column(String)
    
    created_at = Column(DateTime, default= datetime.utcnow)
    
    telemetries = relationship("Telemetry", back_populates="agent")
    
class Telemetry(Base):
    __tablename__ = "telemetry"
    
    id = Column(Integer, primary_key=True, index= True)
    
    cpu = Column(Float) #why Float and not float?
    
    ram = Column(Float)
    
    disk = Column(Float)
    
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    
    
    
    
    
    
    