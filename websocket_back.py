import asyncio
import websockets
import json
from epilepsyTracker import open_stream

async def echo(websocket, path):
    async for message in websocket:
        # data = json.loads(message)
        data = message
        print("received data:", data)
        print(data)
        response = json.dumps({"status": "Received"})
        await websocket.send(response)
        await open_stream(data, websocket)
# client_ip = websockets.getspeername()

start_server = websockets.serve(echo, "172.20.209.75", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
