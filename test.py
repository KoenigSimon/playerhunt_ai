import data_model as data
import command_structure as cmd
import math_helper as math
import game_logic as logic


if __name__ == '__main__':
    data.game_data = data.GameData()
    
    teststrings = [ "player_pos [7.5;0;5]",
                    #"play_area [10;10]",
                    "cell_size [5;5]",
                ]

    for str in teststrings:
        written_field = logic.parse_input_data(str)
        print(f"Parsed Data: {data.game_data.__getattribute__(written_field)}")

    print(math.position_to_grid(data.game_data.player_pos, data.game_data.cell_size))
