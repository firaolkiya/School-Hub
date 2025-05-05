
from fastapi import WebSocket
from .message import Message
from collections import defaultdict
from typing import DefaultDict

class ConnectionManager:
    def __init__(self):
        self.active_connections: DefaultDict[int, list[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket,section_id:str):
        await websocket.accept()
        self.active_connections[section_id].append(websocket)

    def disconnect(self, websocket: WebSocket,section_id:str):
        self.active_connections[section_id].remove(websocket)

    async def send_personal_message(self, message: Message, websocket: WebSocket):
        await websocket.send(message)
    async def broadcast(self, message: Message,section_id:int):
        for connection in self.active_connections[section_id]:
            await connection.send(message)
