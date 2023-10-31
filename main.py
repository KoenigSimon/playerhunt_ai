import asyncio
import websockets

import gpt_interface as gpt
import command_structure as cmd
import game_logic as logic

async def on_connect(websocket):
    """
    This method is called whenever a new client connects.
    """
    print(f"New client connected: {websocket.remote_address}")
    # You can add more logic here if you want, like sending a welcome message:
    # await websocket.send("Welcome to the WebSocket server!")

async def handler(websocket, path):
    await on_connect(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            action = logic.parse_input_data(message)


            # Generate a response (you can modify this logic as needed)
            response = f"Hello! You said: {message}"

            # Send the response back to the client
            await websocket.send(response)

    except websockets.ConnectionClosed:
        print("Connection closed")

if __name__ == '__main__':
    # Prepare GPT messaging backend
    global messages 
    messages = cmd.init_command_structure()
    gpt.consult_ai()

    # Init game logic
    

    # Start the WebSocket server
    start_server = websockets.serve(handler, "localhost", 6969)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
