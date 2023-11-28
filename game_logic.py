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
    
    # dependencies are rendered here:
    condition_lookup_dict = {
        "NOISE_POSITION": [ {"noise_position", "cell_size", math.position_to_grid} ],
        "SELF_POSITION": [ {"self_pos", "cell_size", math.position_to_grid} ],
        "PLAYER_DISTANCE": [ {"target_pos", "self_pos", distance_state} ],
        "LOOK_AT_STATE": [ {"target_heading", "self_heading", look_at_state} ],
    }
    return condition_lookup_dict[abstract_condition]

def distance_state(self_pos: data.Vector3, target_pos: data.Vector3):
    distance = math.distance(self_pos, target_pos)
    if distance < data.game_data.distance_near:
        return "very close to the player"
    elif distance < data.game_data.distance_mid:
        return "close to the player"
    elif distance < data.game_data.distance_far: 
        return "further away, but still in hearing distance to the player"
    else:
        return "far away from the player, not being able to sense them"

def look_at_state(self_head: data.Vector3, target_head: data.Vector3) -> str:
    look_at_factor = math.look_at_factor(self_head, target_head)
    if look_at_factor > data.game_data.lookat_direct:  # in fov
        return "looks directly at you"
    elif look_at_factor > data.game_data.lookat_periph:
        return "might see you if you come out of hiding"
    else: 
        return "looks away from you"

def consider_action():
    #when self_position is 0 -> uninitialized
    #restart restarts with new context

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