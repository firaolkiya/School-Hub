from sqlalchemy import String,ForeignKey,TIMESTAMP,Integer,text,Column

from .section import Base
class Chat(Base):
    __tablename__="chat"
    
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String,nullable=True)
    section_id = Column(Integer,ForeignKey("section.id"))
    created_at = Column(TIMESTAMP,server_default=text('now()'))
    updated = Column(TIMESTAMP,server_default=text('now()'))
    