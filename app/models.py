from sqlalchemy import Column, Integer, String, DateTime
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
    
    created_at = Column(DateTime, default= datetime.utcnow)
    
    