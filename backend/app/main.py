from fastapi import FastAPI,status
from student.routers import auth
app = FastAPI()

app.include_router(auth.router)
@app.get("/",status_code=status.HTTP_200_OK)
def index():
    return {"message":"School management system"}
