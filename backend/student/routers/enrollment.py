from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..utils.database import get_db
from ..models import courses as model
from ..schemas import enlrollement as enrollSchema
from ..models.enrollment import Enrollment as EnrollModel
from ..models.students import Student
from ..models.courses import Course
from ..schemas.course import CourseOut
router = APIRouter(
    prefix='/enrolls',
    tags=['Enrollments']
)



@router.post('/',status_code=status.HTTP_201_CREATED)
def enroll_course(info:enrollSchema.Enrollment,db:Session=Depends(get_db)):
    
    user = db.query(Student).filter(Student.id==info.stud_id)
    
    if not user.first():
        raise HTTPException(
            detail="User doesn't found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    course = db.query(model.Course).filter(model.Course.id==info.course_id)
    
    if not course.first():
        raise HTTPException(
            detail="Course doesn't found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    enrollment = EnrollModel(**info.model_dump())
    db.add(enrollment)
    db.commit()
    return {
        "message":"successfully enrolled course"
    }


@router.delete('/',status_code=status.HTTP_204_NO_CONTENT)
def drop_course(stud_id:str,course_id:int,db:Session=Depends(get_db)):
    enrolled = db.query(EnrollModel).filter(EnrollModel.course_id==course_id and EnrollModel.stud_id==stud_id)
    
    if not enrolled.first():
        raise HTTPException(
            detail='course not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    enrolled.delete(synchronize_session=False)
    db.commit()
    return {"message":"dropped succesfully"}


@router.get('/all',response_model=list[enrollSchema.EnrollmentOut])
def get_all_enrolled_course(db:Session = Depends(get_db)):
    
    enrollments = db.query(Student,Course
                           ).join(EnrollModel,EnrollModel.stud_id==Student.id).join(
                               Course,Course.id==EnrollModel.course_id
                               ).all()
    result = [{"student": student, "course": course} for student, course in enrollments]
 
    return result


@router.get('/students',response_model=enrollSchema.EnrollCourseOut)
def get_enrolls_for_student(stud_id:str,db:Session = Depends(get_db)):
    
    enrollments = db.query(
        Course,
    ).join(
        EnrollModel, EnrollModel.stud_id == stud_id
    ).all()
    result={
        'courses':enrollments,
        'total_course':len(enrollments),
        'total_credit_hours':sum(cr.credit_hour for cr in enrollments)
    }
    return result

@router.get('/',response_model=enrollSchema.StudentEnrollOut)
def get_enrolls_by_course(course_id:int,db:Session = Depends(get_db)):
    
    enrollments = db.query(Student).filter(EnrollModel.course_id==course_id).all()
    result = {
        'students':enrollments,
        'total_students':len(enrollments)
    }
    return result
