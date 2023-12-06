import asyncio
import websockets
import time
import threading

import gpt_interface as gpt
import command_structure as cmd
import data_model as data
import game_logic as logic
import math_helper as math

async def on_connect(websocket):
    print(f"New client connected: {websocket.remote_address}")

def print_console_output(data):
    #reserve 10 lines
    cnt = 0
    for i in data:
        print("\r" + str(i))
        cnt += 1
        if cnt > 10: return
        pass
    print(f'\033[{cnt}A')
    pass

async def handler(websocket, path):
    await on_connect(websocket)
    try:
        async for message in websocket:
            # Data ingest
            target_field = logic.parse_input_data(message)
            response = f"Parsed {target_field}: {data.game_data.__getattribute__(target_field)}"
            data.console_state[1] = response
            print_console_output(data.console_state)

            # send over entire datastructure lol
            for p in logic.all_props(data.game_data):
                msg = f"{p} {str(data.game_data.__getattribute__(p))}"
                print(msg)
                await websocket.send(msg)

            #await websocket.send(str(response))
            pass
    except websockets.ConnectionClosed:
        print("Connection closed")

if __name__ == '__main__':
    # Init game logic
    print("Preparing Game Logic and Parsers")
    data.game_data = data.GameData()

    # Prepare GPT messaging backend
    print("Preparing GPT Backend")
    data.messages = cmd.init_command_structure()    

    # Start the WebSocket server
    print("Starting Server")
    start_server = websockets.serve(handler, "0.0.0.0", 6969)

    #Crude console logging
    data.console_state = [ "" for i in range(10) ]
    data.console_state[0] = "Data State and Debug:"
    print_console_output(data.console_state)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    print('\n\n\n\n\n\n\n\n')
