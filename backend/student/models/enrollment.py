from sqlalchemy import Column, String, Integer,ForeignKey
from .chat import Base

class Enrollment(Base):
    __tablename__ = 'enrollment'
    stud_id = Column(String,ForeignKey('student.id',ondelete="CASCADE"),primary_key=True)
    course_id = Column(Integer,ForeignKey('courses.id',ondelete="CASCADE"),primary_key=True)
    