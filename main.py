import asyncio
import websockets

import gpt_interface as gpt
import command_structure as cmd
import data_model as data
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
            print(f"Received data: {message}")
            if message.startswith("#gpt"):
                prompt = message.removeprefix("#gpt").strip()
                data.messages.append({"role": "user", "content": prompt})
                answer = gpt.consult_ai(data.messages)
                data.messages.append(answer)
                response = answer['content']
            else:
                print(f"Parsing input message: {message}")
                target_field = logic.parse_input_data(message)
                # Generate a response (you can modify this logic as needed)
                response = f"Parsed Data: {data.game_data.__getattribute__(target_field)}"

            await websocket.send(response)

    except websockets.ConnectionClosed:
        print("Connection closed")

if __name__ == '__main__':
    # Prepare GPT messaging backend
    print("Preparing GPT Backend")
    data.messages = cmd.init_command_structure()
    
    # Init game logic
    print("Preparing Game Logic and Parsers")
    data.game_data = data.GameData()

    # Start the WebSocket server
    print("Starting Server")
    start_server = websockets.serve(handler, "0.0.0.0", 6969)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
