import data_model as data

control_context = """You control the behaviour of a game AI. Your goal is to hunt the player. When queried you respond with the options written in capital letters. Queries contain additional information that will help you decide.
You you can use the previous queries to adjust your behaviour. When you charge, you are briefly faster than the player, but they can hear you.
When you sneak closely to the player, they cannot hear you.
"""

# TODO: configuration: set speeds for CHARGE / SNEAK / RUN etc

query_opts = {}

def init_command_structure():
    global query_opts
    query_opts = {
    "attack_decision": f"You are #PLAYER_DISTANCE<{data.game_data.distance_near}# to the player, the player #TARGET_LOOK_SELF_STATE>{data.game_data.lookat_direct}#, do FLEE and try again later or do you jump at the player to win?",
    "proximity_decision": f"You are #PLAYER_DISTANCE<{data.game_data.distance_far}#, the player #TARGET_LOOK_SELF_STATE#. Regarding this information, do you SNEAK after the player and quietly follow them, turn around and FLEE or do you JUMP at the player to win?",
    "investigate_noise": f"You hear a noise at #NOISE_POSITION#, you are at #SELF_POSITION#. You can move one sqare, do you move UP, DOWN, LEFT or RIGHT?",  
    "wander": f"The player is not in sight, do you wander UP, DOWN, LEFT, RIGHT, or do you WAIT until you see the player? Do you maybe remember information on how to find them? Choose one direction",

    #"player_confrontation": "You see the player and the player sees you. Do you CHARGE at the player to catch them and win or RUN away?",
    #"player_discovery": "You see the player, but they are facing away from you. Do you CHARGE at the player to catch them or SNEAK after them to get closer?",
    #player spotted you
    }

    messages=[
        {"role": "system", "content": 
        """You control the behaviour of a game AI. Your goal is to hunt the player. When queried you respond with the options written in capital letters. Queries contain additional information that will help you decide.
        You you can use the previous queries to adjust your behaviour.
        """},
        #{"role": "user", "content": "You enter a dark forest, search for the player and catch or attack them to win."},
    ]
    return messages

def limit_context(messages, count):
    init_message = messages.pop(0) #keep init message
    return [init_message] + messages[-count:]

def return_log(messages):
    out = "The Story:\n"
    for msg in messages:
        if msg['role'] == 'user':
            out += "Narrator: " + msg['content'] + "\n"
        if msg['role'] == 'assistant':
            out += "AI: " + msg['content'] + "\n"