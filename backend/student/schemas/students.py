from pydantic import BaseModel,EmailStr
from typing import Optional

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


class LoginSchema(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    token_type:str
    access_token:str
