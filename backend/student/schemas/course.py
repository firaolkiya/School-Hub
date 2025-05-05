from pydantic import BaseModel
from typing import Optional


class CourseIn(BaseModel):
    name:str
    code:str
    credit_hour:int
    
    
class CourseOut(BaseModel):
    name:str
    code:str
    credit_hour:int
    id:int

    
class CourseUpdate(BaseModel):
    name:Optional[str]=''
    code:Optional[str]=''
    credit_hour:Optional[int]=-1
    id:int