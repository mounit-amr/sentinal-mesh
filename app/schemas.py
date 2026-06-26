from sqlalchemy import column, Integer, String, DateTime
from datetime import datetime#dont know why redlines

class user(Base):
    __tablename__ = "user"
    
    id = column(Integer, primary_key = True, index = True)
    
    name = column(String, unique = false )
    
    role = column(String) 
    
    email = column(String, unique = True)
    