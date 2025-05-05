from pydantic import BaseModel
from .course import CourseOut
from .students import StudentOut

class Enrollment(BaseModel):
    stud_id:str
    course_id:int
    

    
class EnrollmentOut(BaseModel):
    student:StudentOut
    course:CourseOut

class StudentEnrollOut(BaseModel):
    total_students:int
    students:list[StudentOut]

class EnrollCourseOut(BaseModel):
    total_credit_hours:int
    total_course:int
    courses:list[CourseOut]