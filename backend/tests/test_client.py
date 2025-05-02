from .database import client,session

def test_root(client):
    res = client.get("/")
    print("testing root")
    message = res.json()["message"]
    assert message=="School management system"    
    


def test_student_signup(client):
    result = client.post(
        "/students/signup",
        json={
           "first_name":"firaol",
           "email":"email@gmail.com",
            "last_name":"kiyebu",
            "middle_name":"klo",
            "nationality":"Eth",
            "age":0,
            "class_year":0,  
            "department":"SEn" 
         }
    )
    
    assert result.status_code==201