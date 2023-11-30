import data_model as data
import command_structure as cmd
import math_helper as math
import game_logic as logic


if __name__ == '__main__':
    data.game_data = data.GameData()

    logic.parse_input_data("cell_size [0.5;0.5]")
    logic.parse_input_data("target_pos [1;1;1]")
    logic.parse_input_data("self_pos [1;1;1]")
    logic.parse_input_data("target_heading [0.5;0;0.5]")
    logic.parse_input_data("self_heading [1;0;0]")
    logic.parse_input_data("noise_position [1;2;3]")
    
    logic.consider_action()

    print(math.position_to_grid(data.game_data.target_pos, data.game_data.cell_size))
