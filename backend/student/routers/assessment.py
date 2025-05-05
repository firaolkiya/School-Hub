from fastapi import APIRouter,Depends,HTTPException,status
from ..utils.database import get_db
from sqlalchemy.orm import Session
from ..models import assessment as model
from ..schemas import assessment as scheama
from datetime import datetime
from ..models.students import Student
router = APIRouter(
    prefix='/assessments',
    tags=['Assessments']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def record_assessment(assessment:scheama.FillAssessment,db:Session=Depends(get_db)):
    
    new_assessment = model.Assessment(**assessment.model_dump())
    
    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)
    return new_assessment


@router.put('/')
def update_assessment(assessment:scheama.UpdateAssessment,db:Session=Depends(get_db)):
    
    current_assessment = db.query(model.Assessment).filter(model.Assessment.id==assessment.id)
    if not current_assessment.first():
        raise HTTPException(
            detail='The assessment either deleted or invalid id',
            status_code=status.HTTP_404_NOT_FOUND
        )
    maps = assessment.model_dump()
    updated_data = {key:maps[key] for key in maps if maps[key]>-1}
    updated_data['updated_at']=datetime.now()
    current_assessment.update(updated_data,synchronize_session=False)
    db.commit()
    return current_assessment.first()


@router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete_assessment(id:int,db:Session=Depends(get_db)):
    
    current_assessment = db.query(model.Assessment).filter(model.Assessment.id==id)
    if not current_assessment.first():
        raise HTTPException(
            detail='The assessment either deleted or invalid id',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    current_assessment.delete(synchronize_session=False)
    db.commit()
    return {
        'message':'deleted successfully'
    }

@router.get('/{stud_id}')
def get_all_assessment(stud_id:str,db:Session=Depends(get_db)):
    assessments = db.query(model.Assessment).filter(
        model.Assessment.stud_id==stud_id 
        ).all()
    return assessments

@router.get('/current/{stud_id}')
def get_semister_assessment(stud_id:str,db:Session=Depends(get_db)):
    student = db.query(Student).filter(Student.id==stud_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='invalid student id'
        )
    assessments = db.query(model.Assessment).filter(
        model.Assessment.stud_id==stud_id 
        and model.Assessment.semester==student.current_accedemic_semister
        ).all()
    return assessments

@router.get('/courses')
def get_assessment_for_course(stud_id:str,course_id:int,db:Session=Depends(get_db)):
    assessment = db.query(model.Assessment).filter(
        model.Assessment.course_id==course_id and model.Assessment.stud_id==stud_id
    ).all()
    return assessment


@router.post('/complaints')
def complain_course(stud_id:str,course_id:int,db:Session=Depends(get_db)):
    pass

