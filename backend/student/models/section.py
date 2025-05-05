from sqlalchemy import String,Integer,ForeignKey,Column,text,TIMESTAMP
from .assessment import Base
class Section(Base):
    __tablename__="section"
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True,unique=True)
    name = Column(String,primary_key=True,nullable=False,unique=True)
    representative =Column(String,ForeignKey('student.id',ondelete='SET NULL'),nullable=True)
    max_capacity = Column(Integer,server_default=text('100'))
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'))

