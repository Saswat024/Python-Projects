from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from typing import Dict, Set

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Store active connections
active_connections: Dict[str, Set[WebSocket]] = {}


@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws/{username}/{room}")
async def websocket_endpoint(websocket: WebSocket, username: str, room: str):
    await websocket.accept()

    # Add connection to the room
    if room not in active_connections:
        active_connections[room] = set()
    active_connections[room].add(websocket)

    # Notify room about new user
    await broadcast_to_room(
        {
            "sender": "System",
            "message": f"{username} has joined the chat",
            "room": room,
        },
        room,
    )

    try:
        while True:
            data = await websocket.receive_text()
            await broadcast_to_room(
                {**json.loads(data), "sender": username, "room": room}, room
            )
    except WebSocketDisconnect:
        active_connections[room].remove(websocket)
        if not active_connections[room]:
            del active_connections[room]
        await broadcast_to_room(
            {
                "sender": "System",
                "message": f"{username} has left the chat",
                "room": room,
            },
            room,
        )


async def broadcast_to_room(message: dict, room: str):
    if room in active_connections:
        for connection in active_connections[room]:
            try:
                await connection.send_json(message)
            except:
                continue


def get_room_users(room: str):
    if room in active_connections:
        return len(active_connections[room])
    return 0


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
