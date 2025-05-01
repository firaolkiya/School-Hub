from pydantic import BaseModel
from typing import Optional

class RegisterStudent(BaseModel):
    first_name:str
    last_name:str
    middle_name:str
    nationality:str
    age:int
    class_year:int
    school:Optional[str]
    admission:str="Undergraduate Full time"
    department:str

