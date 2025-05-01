from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session
from ..schemas.students import RegisterStudent
from ..utils.database import get_db
from ..models import students
from datetime import date

from ..utils.password import hash_password,generete_password

router = APIRouter(
    prefix="/students"
)

def generate_user_id(db:Session=Depends(get_db)):
    yt = date.today().year-200
    cur_studs = db.query(students.Student).filter(students.Student.id.endswith(str(yt)))
    m_id = len(cur_studs)+1000 if cur_studs  else 1000
    return f"UGR/{m_id}/{yt}"
    
@router.get("/")
def get_all_students(db:Session=Depends(get_db)):
    studens = db.query(students.Student).all()
    return studens

@router.post("/",status_code=status.HTTP_201_CREATED)
def register_student(student:RegisterStudent,db:Session=Depends(get_db)):
    # generate user id
    yt = date.today().year-2000
    cur_studs = db.query(students.Student).filter(students.Student.id.endswith(str(yt))).all()
    m_id = len(cur_studs)+1000 if cur_studs  else 1000
    stud_id= f"UGR/{m_id}/{yt}"
    plain_password = generete_password(student.first_name)
    password = hash_password(plain_password)
    db_student = students.Student(**student.dict(),id=stud_id,password=password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db_student.password = plain_password
    return db_student
    