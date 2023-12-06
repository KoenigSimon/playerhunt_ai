import data_model as data
import command_structure as cmd
import math_helper as math
import game_logic as logic


if __name__ == '__main__':
    data.game_data = data.GameData()
    data.messages = cmd.init_command_structure()

    logic.parse_input_data("cell_size [0.5;0.5]")
    logic.parse_input_data("target_pos [1;1;1]")
    logic.parse_input_data("self_pos [1;1;1]")
    logic.parse_input_data("target_heading [0.5;0;0.5]")
    logic.parse_input_data("self_heading [1;0;0]")
    logic.parse_input_data("noise_position [1;2;3]")
    
    results = logic.consider_action()
    for r in results:
        print(r)

    #expr = logic.parse_option_expression(f"ababab #PLAYER_DISTANCE<{data.game_data.distance_far}# ususus")
    #string = expr[0]
    #print(string)
#
    #condition = logic.find_capital_words(string)[0]
    #print(logic.literate_condition(condition))
    #string = string.replace(condition, str(logic.literate_condition(condition)[0][0]))
    #print(string)
    #print(eval(string))