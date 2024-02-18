import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        print("received data:", data)
        response = json.dumps({"status": "Received"})
        await websocket.send(response)

# client_ip = websockets.getspeername()

start_server = websockets.serve(echo, "192.168.64.1", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
