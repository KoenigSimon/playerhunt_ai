import re

import data_model as data
import command_structure as cmd
import math_helper as math

def resolve_condition_dependencies(condition_str: str):
    # takes complex conditions and returns required data fields and corresponding functions
    # calc function, depending data...
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
        return (distance, "very close to the player so you can catch him with one jump")
    elif distance < data.game_data.distance_mid:
        return (distance, "close to the player, so that you have to charge a short distance and might give the player a chance to get away")
    elif distance < data.game_data.distance_far: 
        return (distance, "further away, but still in hearing distance to the player")
    else:
        return (distance, "far away from the player, not being able to sense them")

def look_at_state(self_head: data.Vector3, target_head: data.Vector3) -> str:
    look_at_factor = math.look_at_factor(self_head, target_head)
    if look_at_factor > data.game_data.lookat_direct:  # in fov
        return (look_at_factor, "looks directly at you, making hiding and sneaking impossible")
    elif look_at_factor > data.game_data.lookat_periph:
        return (look_at_factor, "might see you if you come out of hiding")
    else: 
        return (look_at_factor, "looks away from you")
    
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

def parse_option_expression(action: str) -> [str]:
    # This regular expression looks for any non-whitespace characters between # symbols
    pattern = r"#(\S+?)#"
    conditions = re.findall(pattern, action)
    return conditions

def find_capital_words(text) -> [str]:
    # This regular expression looks for any non-whitespace characters between # symbols
    pattern = r'\b[A-Z_]{2,}\b'
    capital_words = re.findall(pattern, text)
    return capital_words

def literate_condition(condition_str:str):
    results = []
    for condition in resolve_condition_dependencies(condition_str):
        results.append(condition[0](*condition[1:]) )
    return results

def consider_action() -> [tuple]:
    #when self_position is 0 -> uninitialized
    #restart restarts with new context, purge gpt history

    #when collected enough data
    #consider action from command structure
    valid_query_opts = []
    for query_option, action in cmd.query_opts.items():
        action_valid = True
        for abstract_expression in parse_option_expression(cmd.query_opts[query_option]):
            abstract_condition = find_capital_words(abstract_expression)[0]
            for dependency in resolve_condition_dependencies(abstract_condition):
                for dict_field in dependency:
                    #check for each abstract condition if all fields are present in the data model
                    #if so, add to valid options
                    if not callable(dict_field) and dict_field == 0: #not callable ignores the function
                        action_valid = False
            if action_valid:
                # action valid means all required data is present
                resolved_conditions = literate_condition(abstract_condition)
                expression = abstract_expression.replace(abstract_condition, str(resolved_conditions[0][0]))
                #if evaluated expression is of type bool AND true, add to valid actions
                if eval(expression) is False:
                    action_valid = False
                action = action.replace(f"#{abstract_expression}#", " ".join(str(x[1]) for x in literate_condition(abstract_condition)))
        if action_valid: 
            valid_query_opts.append( (query_option, action) )

    if len(valid_query_opts) == 0: print("No valid options found D:") #wander should always be possible
    return valid_query_opts

def validate_action(action):
    #stub
    pass