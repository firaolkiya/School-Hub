from sqlalchemy import Column, String, Integer,ForeignKey,text,Double
from sqlalchemy.orm import relationship
from .chat import Base

class Enrollment(Base):
    __tablename__ = 'enrollment'
    stud_id = Column(String,ForeignKey('student.id',ondelete="CASCADE"),primary_key=True)
    course_id = Column(Integer,ForeignKey('courses.id',ondelete="CASCADE"),primary_key=True)
    grade = Column(Double,server_default=text('0'))
    status = Column(String,server_default='Taking')
    total_score = Column(Double,server_default=text('0'))
    total_max_score = Column(Double,server_default=text('100'))
    student=relationship("Student", back_populates="enrolls")
    course = relationship("Course")
    