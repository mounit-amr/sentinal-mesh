from fastapi import FastAPI, WebSocket, Depends #whats the difference between Websocket and websockets
from database import gent

app = FastAPI()

@app.get("/")
def value():
    return {"online"}

@app.post("/telemetry")
def authen(agent : Agent = Depends(authenticate)):
    pass
@app.websocket("/ws")
async def websocks(websockets: WebSocket):
    await websockets.accept()
    try:
        while True:
            data = await websockets.receive()
            
            await websockets.send(data)
            
    except :
        print("offline")
        


