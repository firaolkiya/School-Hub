from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..models import section as model
from ..schemas import section as schema

router = APIRouter(
    prefix='/sections',
    tags=['Sections']
)


@router.post('/',response_model=schema.SectionOut,status_code=status.HTTP_201_CREATED)
def add_section(section:schema.SectionIn,db:Session=Depends(get_db)):
    
    new_section = model.Section(**section.model_dump())
    
    db.add(new_section)
    db.commit()
    db.refresh(new_section)
    
    return new_section


@router.put('/',response_model=schema.SectionOut,status_code=status.HTTP_201_CREATED)
def update_section(up_section:schema.SectionUpdate,db:Session=Depends(get_db)):
    
    sections = db.query(model.Section).filter(model.Section.id==up_section.id)
    
    if not sections.first():
        raise HTTPException(
            detail='section not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    to_update = {
    }
    if up_section.name!='':
        to_update['name']=up_section.name
    if up_section.max_capacity!=-1:
        to_update['max_capacity']=up_section.max_capacity
   
    sections.update(to_update,synchronize_session=False)
    db.commit()
    
    return sections.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_section(id:int,db:Session=Depends(get_db)):
    sections = db.query(model.Section).filter(model.Section.id==id)
    
    if not sections.first():
        raise HTTPException(
            detail='section not found',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    sections.delete(synchronize_session=False)
    db.commit()
    return {"msg":"section deleted"}


@router.get('/',response_model=list[schema.SectionOut])
def get_all_sections(db:Session=Depends(get_db)):
    
    sections = db.query(model.Section).all()
    return sections
