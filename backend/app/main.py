from fastapi import FastAPI,status
from student.routers import auth,course,section,enrollment,assessment,chat
app = FastAPI()

app.include_router(auth.router)
app.include_router(course.router)
app.include_router(section.router)
app.include_router(enrollment.router)
app.include_router(assessment.router)
app.include_router(chat.router)


@app.get("/",status_code=status.HTTP_200_OK)
def index():
    return {"message":"School management system"}
