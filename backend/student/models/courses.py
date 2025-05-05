
from sqlalchemy import Column, String, Integer,TIMESTAMP,text

from ..utils.database import Base


class Course(Base):
    __tablename__ = "courses"
    
    name=Column(String,nullable=False)
    code=Column(String,nullable=False,unique=True)
    id= Column(Integer,nullable=False,primary_key=True,index=True,autoincrement=True,unique=True)
    credit_hour= Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP,server_default=text('now()'))

