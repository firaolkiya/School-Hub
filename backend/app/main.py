from fastapi import FastAPI,status
from student.routers import auth,course,section,enrollment,assessment
app = FastAPI()

app.include_router(auth.router)
app.include_router(course.router)
app.include_router(section.router)
app.include_router(enrollment.router)
app.include_router(assessment.router)


@app.get("/",status_code=status.HTTP_200_OK)
def index():
    return {"message":"School management system"}
