from sqlalchemy import String,Integer,Column,text,TIMESTAMP,Double,ForeignKey
from .message import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "student"
    id = Column(String,primary_key=True)
    email = Column(String,nullable=False,unique=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    middle_name = Column(String,nullable=False)
    nationality = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    current_accedemic_year =   Column(Integer,server_default=text("1"))
    current_accedemic_semister =   Column(Integer,server_default=text("1"))
    status =   Column(String,server_default="Active")
    school = Column(String,nullable=False)
    admission = Column(String,nullable=False)
    department = Column(String,nullable=False)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('now()'))
    gpa = Column(Double,nullable=False,server_default=text('0.0'))
    profile_url = Column(String, nullable=True)
    password = Column(String, nullable=False)
    section_id = Column(Integer,ForeignKey('section.id',ondelete="SET NULL"))
    enrolls=relationship("Enrollment", back_populates="student")

    
