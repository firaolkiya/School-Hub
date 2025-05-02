from pydantic import BaseModel,EmailStr
from typing import Optional
from ..utils.password import generete_password
class RegisterStudent(BaseModel):
    first_name:str
    email:EmailStr
    last_name:str
    middle_name:str
    nationality:str
    age:int
    class_year:int  
    school:Optional[str]="Pre school"
    admission:Optional[str]="Undergraduate Full time"
    department:str

