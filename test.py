import asyncio
import time

import data_model as data
import command_structure as cmd
import math_helper as math
import game_logic as logic
import main
import gpt_interface as gpt

def create_ai_task():
    return asyncio.create_task(gpt.consult_ai(data.messages))

async def main():
    task = create_ai_task()
    cmd.add_user_message("The player is not in sight, do you wander UP, DOWN, LEFT, RIGHT, or do you WAIT until you see the player? Do you maybe remember information on how to find them? Choose one direction")
    print(time.strftime("%H:%M:%S"))
    while True:
        if task.done():
            ai_decision = await task
            print(ai_decision)
            task = create_ai_task()
        print(time.strftime("%H:%M:%S"))
        await asyncio.sleep(0.3)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data.game_data = data.GameData()
    data.messages = cmd.init_command_structure()

    data.console_state = [ "" for i in range(10) ]
    data.console_state[0] = "Data State and Debug:"

    logic.parse_input_data("cell_size [0.5;0.5]")
    logic.parse_input_data("target_pos [1;1;1]")
    logic.parse_input_data("self_pos [1;1;1]")
    logic.parse_input_data("target_heading [0.5;0;0.5]")
    logic.parse_input_data("self_heading [1;0;0]")
    logic.parse_input_data("noise_position [1;2;3]")
    
    #results = logic.consider_action()
    #for r in results:
    #    print(r)

    asyncio.run(main())