from fastapi import File,UploadFile
from pydantic import BaseModel,EmailStr,EncodedBytes
from typing import Annotated, Optional

from sqlalchemy import null

class RegisterStudent(BaseModel):
    first_name:str
    email:EmailStr
    last_name:str
    middle_name:str
    nationality:str
    age:int
    current_accedemic_year:int  
    school:Optional[str]="Pre school"
    admission:Optional[str]="Undergraduate Full time"
    department:str
    current_accedemic_semister:int
class UpdateProfile(BaseModel):
    stud_id:str
    file:Optional[UploadFile]=File(...)
class StudentOut(RegisterStudent):
    id:str
    status:str
    profile_url:Optional[str]=null


class LoginSchema(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    token_type:str
    access_token:str
