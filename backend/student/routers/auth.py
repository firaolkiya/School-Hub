from fastapi import APIRouter,status
from ..schemas.students import RegisterStudent
router = APIRouter(
    prefix="/students"
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def register_student(student:RegisterStudent):
    return student