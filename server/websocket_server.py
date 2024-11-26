import asyncio
import websockets
import json

# Track connected clients
connected_clients = set()

async def handle_client(websocket):
    print(f"New client connected: {websocket}")
    

    connected_clients.add(websocket)

    await websocket.send(json.dumps({
            "question": "Explain about AI?"
        }))

async def server():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(server())
