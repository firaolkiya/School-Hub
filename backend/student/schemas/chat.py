from pydantic import BaseModel


class CreateChat(BaseModel):
    name:str
    