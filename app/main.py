from fastapi import FastAPI, WebSocket #whats the difference between Websocket and websockets


app = FastAPI()

@app.get("/")
def value():
    return {"online"}
    
@app.websocket("/ws")
async def websocks(websockets: WebSocket):
    await websockets.accept()
    try:
        while True:
            data = await websockets.receive()
            
            await websockets.send(data)
            
    except :
        print("offline")
        
            