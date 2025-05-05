from sqlalchemy import String,Integer,Column,text,TIMESTAMP,Double,ForeignKey
from .courses import Base
class Score(Base):
    __tablename__="score"
    id=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    teacher_id = Column(String,nullable=False)
    stud_id = Column(String,ForeignKey("student.id",ondelete="CASCADE"))
    course_id = Column(Integer,ForeignKey("courses.id",ondelete="SET NULL"))
    point = Column(Double,nullable=False)
    created_at = Column(TIMESTAMP,server_default=text("now()"))
    updated_at = Column(TIMESTAMP,server_default=text("now()"))
    


    
    
    