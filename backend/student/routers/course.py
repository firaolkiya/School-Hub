from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..models import courses as model
from ..schemas import course as schema

router = APIRouter(
    prefix='/courses',
    tags=['Courses']
)


@router.post('/',response_model=schema.CourseOut,status_code=status.HTTP_201_CREATED)
def add_course(course:schema.CourseIn,db:Session=Depends(get_db)):
    
    new_course = model.Course(**course.model_dump())
    
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    
    return new_course


@router.put('/',response_model=schema.CourseOut,status_code=status.HTTP_201_CREATED)
def update_course(up_course:schema.CourseUpdate,db:Session=Depends(get_db)):
    
    courses = db.query(model.Course).filter(model.Course.id==up_course.id)
    
    if not courses.first():
        raise HTTPException(
            detail='course not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    to_update = {
    }
    if up_course.code!='':
        to_update['code']=up_course.code
    if up_course.name!='':
        to_update['name']=up_course.name
    if up_course.credit_hour!=-1:
        to_update['credit_hour']=up_course.credit_hour
   
    courses.update(to_update,synchronize_session=False)
    db.commit()
    
    return courses.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id:int,db:Session=Depends(get_db)):
    courses = db.query(model.Course).filter(model.Course.id==id)
    
    if not courses.first():
        raise HTTPException(
            detail='course not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    courses.delete(synchronize_session=False)
    db.commit()
    return {"msg":"course deleted"}


@router.get('/',response_model=list[schema.CourseOut])
def get_all_courses(db:Session=Depends(get_db)):
    
    courses = db.query(model.Course).all()
    return courses
    