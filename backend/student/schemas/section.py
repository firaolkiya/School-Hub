from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SectionIn(BaseModel):
    name:str
    max_capacity:int
    
    
class SectionOut(BaseModel):
    name:str
    max_capacity:int
    id:int
    created_at:datetime
    updated_at:datetime

    
class SectionUpdate(BaseModel):
    name:Optional[str]=''
    max_capacity:Optional[int]=-1
