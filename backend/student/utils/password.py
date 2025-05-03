from datetime import datetime, timedelta, timezone
from typing import Annotated

from passlib.context import CryptContext
from ..config import setting
from jwt.exceptions import InvalidTokenError
import jwt
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .database import get_db
from  ..models.students import Student

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="students/login")


def generete_password(first_name:str):
    return f"{first_name}123"

def hash_password(plain_password):
    return pwd_context.hash(plain_password)

def verify_password(plain_pass:str,hashed_pass:str):
    return pwd_context.verify(plain_pass,hashed_pass)


async def get_user(username:str,db:Session):
    user = await db.query(Student).filter(Student.id==username)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found") 
    return user.first()

async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, setting.secret_key, algorithms=setting.algorithm)
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except InvalidTokenError as error:
        credentials_exception.detail=error.args
        raise credentials_exception
    #  user = await get_user(username=username,db=db)
    # if user is None:
    #     raise credentials_exception
    # return user

def create_access_token(username: str):
    expire_minutes = int(setting.access_token_expire_minutes)
    expire_time = datetime.now() + timedelta(minutes=expire_minutes)

    to_encode={
                "sub": username, 
                "exp": expire_time
            }
 
    encoded_jwt = jwt.encode(to_encode, setting.secret_key, setting.algorithm)
    return encoded_jwt

