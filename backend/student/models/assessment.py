from sqlalchemy import String,Integer,Column,text,TIMESTAMP,Double,ForeignKey
from .courses import Base
class Assessment(Base):
    __tablename__="assessment"
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    teacher_id = Column(String,nullable=False)
    stud_id = Column(String,ForeignKey("student.id",ondelete="CASCADE"))
    course_id = Column(Integer,ForeignKey("courses.id",ondelete="SET NULL"))
    score = Column(Double,server_default=text("0"))
    max_score = Column(Double,server_default=text("0"))
    semester = Column(Integer,server_default=text("1"))
    student_accedemic_year= Column(Integer,server_default=text("1"))
    created_at = Column(TIMESTAMP,server_default=text("now()"))
    updated_at = Column(TIMESTAMP,server_default=text("now()"))



    
    


    
    
    