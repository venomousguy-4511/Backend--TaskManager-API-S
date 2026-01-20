from sqlalchemy import Column,Boolean,Integer,String
from app.db import Base
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable = False)
    done = Column(Boolean,default = False)