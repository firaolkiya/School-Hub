from fastapi import APIRouter,status,Depends,HTTPException,Header,WebSocket,WebSocketDisconnect
from sqlalchemy.orm import Session
from ..models import chat as model
from ..utils.database import get_db
from ..models.students import Student
from ..models.message import Message
from ..models.connection_manager import ConnectionManager

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.get('/',status_code=status.HTTP_200_OK)
def get_all_chat(db:Session=Depends(get_db)):
    
    chats = db.query(model.Chat).all()
    return chats

manager = ConnectionManager()
@router.websocket('/ws')
async def start_listen(section_id:int,stud_id:str,websocket:WebSocket,db:Session=Depends(get_db)):
    manager.connect(websocket,section_id)
    student = db.query(Student).filter(Student.id==stud_id).first()
    try:
        while True:
            json = await websocket.receive_json()
            message = Message(**json)
            await manager.broadcast(message)
            db.add(message)
            db.commit()
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast(f"Client {student.} left the chat")

