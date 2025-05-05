from sqlalchemy import String,Integer,Column

from .enrollment import Base

class Message(Base):
    __tablename__= "messages"
    id = Column(Integer,autoincrement=True,primary_key=True)
    content = Column(String,nullable=False)

