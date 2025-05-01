from fastapi import FastAPI
from student.routers import auth
app = FastAPI()

app.include_router(auth.router)
@app.get("/")
def index():
    return {"Message":"School; management system"}
