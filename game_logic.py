import re

import data_model as data
import command_structure as cmd
import math_helper as math

def props(cls):   
  return [i for i in cls.__dict__.keys() if i[:1] != '_']

#message supports only one field per message, keep that in mind
def parse_input_data(message: str):
    for name in props(data.game_data):
        if message.startswith(name):
            raw_data = message.removeprefix(name).strip()
            data.game_data.__getattribute__(name).parse(raw_data)
            return name
    print(f"Failed to parse input data for message: {message}")
    return None

def parse_action_condition(action: str):
    # This regular expression looks for any non-whitespace characters between # symbols
    pattern = r"#(\S+?)#"
    conditions = re.findall(pattern, action)
    return conditions

def condition_concretizer(abstract_condition: str):
    #takes complex conditions and returns required data fields and corresponding functions
    condition_lookup_dict = {
        "NOISE_POSITION": [ {"noise_position", "cell_size", math.position_to_grid} ],
        "SELF_POSITION": [ {"self_pos", "cell_size", math.position_to_grid} ],
        "PLAYER_DISTANCE": [ {"player_pos", "self_pos", math.distance} ],
        "LOOK_DIRECTION": [ {"player_heading", "self_pos", math.heading_dir} ],
    }
    return condition_lookup_dict[abstract_condition]

def condition_abstractor(condition_to_abstract: str, data):
    # AI is bad with numbers, translate to words to let it decide
    #stub
    pass

def consider_action():
    #when collected enough data
    #consider action from command structure
    valid_options = []
    for option in cmd.query_opts:
        option_valid = True
        for abstract_cond in parse_action_condition(cmd.query_opts[option]):
            for cond in condition_concretizer(abstract_cond):
                for dict_field in cond:
                    #check for each concrete condition if all fields are present in the data model
                    #if so, add to valid options
                    if type(dict_field) is str and data.game_data.__getattribute__(dict_field) == 0:
                        option_valid = False
        if option_valid: valid_options.append(option)
    
    if len(valid_options) == 0: print("No valid options found, no action taken.")
    else:
        for opt in valid_options:
            print(opt)

    pass

def validate_action(action):
    #stub
    pass

#test
#if __name__ == '__main__':
#    data.game_data = data.GameData()
#    
#    consider_action()