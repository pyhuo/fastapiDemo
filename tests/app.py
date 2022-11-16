import random
import time
import asyncio
import websockets


async def echo(websocket, path):
    while True:
        now = int(time.time())
        await websocket.send(f"{now}: {path}")
        await asyncio.sleep(3)


def main():
    start_server = websockets.serve(echo, "127.0.0.1", 8000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()