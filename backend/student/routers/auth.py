from fastapi import APIRouter,status,Depends,HTTPException,Header
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.security import (
    HTTPBearer,
    OAuth2PasswordRequestForm,
)
from ..schemas import students as schema
from ..utils.database import get_db
from ..models import students as model
from datetime import date

from ..utils.password import (
                              hash_password,
                              generete_password,
                              create_access_token,
                              get_current_user,
                              verify_password,
                              get_user
                              )


router = APIRouter(
    prefix="/students"
)

security = HTTPBearer()
@router.get("/")
def get_all_students(db:Session=Depends(get_db)):
    studens = db.query(model.Student).all()
    return studens

@router.post("/signup",status_code=status.HTTP_201_CREATED)
def register_student(student:schema.RegisterStudent,db:Session=Depends(get_db)):
    # generate user id
    yt = date.today().year-2000
    cur_studs = db.query(model.Student).filter(model.Student.id.endswith(str(yt))).all()
    m_id = len(cur_studs)+1000 if cur_studs  else 1000
    stud_id= f"UGR/{m_id}/{yt}"
    
    # hash password
    plain_password = generete_password(student.first_name)
    password = hash_password(plain_password)
    db_student = model.Student(**student.model_dump(),id=stud_id,password=password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db_student.password = plain_password
    return db_student


@router.post('/login',response_model=schema.Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
          db:Session=Depends(get_db)):
    
    user = db.query(model.Student).filter(model.Student.id==form_data.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"message":"Incorrect email or passwor"})
    
    if not verify_password(form_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"message":"Incorrect email or passwor"})
    access_token = create_access_token(form_data.username)
    
    
    
    return schema.Token(
        token_type="bearer",
        access_token=access_token
    )
    

@router.get("/me",response_model=schema.StudentOut)
def user_info(username:Annotated[model.Student,Depends(get_current_user)],db:Session=Depends(get_db)):
    user =  db.query(model.Student).filter(model.Student.id==username)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user not found") 
    return user.first()
   