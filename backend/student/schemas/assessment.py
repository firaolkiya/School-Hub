from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class FillAssessment(BaseModel):
    teacher_id:str
    stud_id:str
    course_id:int
    max_score:float
    semester:int
    student_accedemic_year:int
    score:float

    
class UpdateAssessment(BaseModel):
    id:int
    max_score:Optional[float]=-1
    semester:Optional[float]=-1
    student_accedemic_year:Optional[int]=-1
    score:Optional[int]=-1

