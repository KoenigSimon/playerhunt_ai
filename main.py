import asyncio
import websockets

import gpt_interface as gpt
import command_structure as cmd
import data_model as data
import game_logic as logic
import math_helper as math

async def on_connect(websocket):
    print(f"New client connected: {websocket.remote_address}")

async def handler(websocket, path):
    await on_connect(websocket)
    try:
        async for message in websocket:
            # Data ingest
            #print(f"Received Data: {message}")
            target_field = logic.parse_input_data(message)
            response = f"Parsed {target_field}: {data.game_data.__getattribute__(target_field)}"
            response = math.position_to_grid(data.game_data.target_pos, data.game_data.cell_size)
            response = f"[{response[0]};{response[1]}]"

            # TODO: send selected action state for debug purposes

            await websocket.send(str(response))

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
