import asyncio
import websockets

async def handler(websocket, path):
    # Loop to keep the connection open and handle messages from the client.
    async for message in websocket:
        print(f"Received message from client: {message}")
        # Send a response back to the client.
        await websocket.send("Message received")
        # Example: Sending multiple responses back to the client.
        await asyncio.sleep(1)  # Simulate some processing time.
        await websocket.send("Processing data")
        await asyncio.sleep(1)  # Simulate more processing time.
        await websocket.send("Data processed")

start_server = websockets.serve(handler, "localhost", 6789)

asyncio.get_event_loop().run(start_server)
# asyncio.get_event_loop().run_forever()
