import asyncio
import websockets


async def server(websocket, path):
    async for message in websocket:
        await websocket.send(message)

start_server = websockets.serve(server, "localhost", 7890)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
