import re

import data_model as data
import command_structure as cmd
import math_helper as math

def resolve_condition_dependencies(condition_str: str):
    # takes complex conditions and returns required data fields and corresponding functions
    # dependencies are rendered here:
    # function, depending data...
    condition_lookup_dict = {
        "NOISE_POSITION": [ (math.position_to_grid, data.game_data.noise_position, data.game_data.cell_size) ],
        "SELF_POSITION": [ (math.position_to_grid, data.game_data.self_pos, data.game_data.cell_size ) ],
        "PLAYER_DISTANCE": [ (distance_state, data.game_data.target_pos, data.game_data.self_pos) ],
        "SELF_LOOK_TARGET_STATE": [ (look_at_state, data.game_data.self_heading, data.game_data.target_heading ) ],
        "TARGET_LOOK_SELF_STATE": [ (look_at_state, data.game_data.target_heading, data.game_data.self_heading ) ],
    }
    return condition_lookup_dict[condition_str]

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
    
##### End of configurable area #####
    
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

def parse_option_conditions(action: str):
    # This regular expression looks for any non-whitespace characters between # symbols
    pattern = r"#(\S+?)#"
    conditions = re.findall(pattern, action)
    return conditions

def literate_condition(condition_str:str):
    results = []
    for condition in resolve_condition_dependencies(condition_str):
        results.append(condition[0](*condition[1:]))
    return results

def consider_action():
    #when self_position is 0 -> uninitialized
    #restart restarts with new context

    #when collected enough data
    #consider action from command structure
    valid_query_opts = []
    for query_option, action in cmd.query_opts.items():
        action_valid = True
        for abstract_condition in parse_option_conditions(cmd.query_opts[query_option]):
            for dependency in resolve_condition_dependencies(abstract_condition):
                for dict_field in dependency:
                    #check for each abstract condition if all fields are present in the data model
                    #if so, add to valid options
                    if not callable(dict_field) and dict_field == 0: #not callable ignores the function
                        action_valid = False
            if action_valid:
                action = action.replace(f"#{abstract_condition}#", " ".join(str(x) for x in literate_condition(abstract_condition)))
        if action_valid: 
            valid_query_opts.append( (query_option, action) )

    if len(valid_query_opts) == 0: print("No valid options found, no action taken.")
    else:
        for opt in valid_query_opts:
            print(opt[0], end=": ")
            print(opt[1])
            pass
        pass
    pass

def validate_action(action):
    #stub
    pass