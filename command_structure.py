control_context = """You control the behaviour of a game AI. Your goal is to hunt the player. When queried you respond with the options written in capital letters. Queries contain additional information that will help you decide.
You you can use the previous queries to adjust your behaviour. When you charge, you are briefly faster than the player, but they can hear you.
When you sneak closely to the player, they cannot hear you.
"""

# TODO: configuration: set speeds for CHARGE / SNEAK / RUN etc

query_opts = {
    #unconditional events
    #"player_confrontation": "You see the player and the player sees you. Do you CHARGE at the player to catch them and win or RUN away?",
    #"player_discovery": "You see the player, but they are facing away from you. Do you CHARGE at the player to catch them or SNEAK after them to get closer?",
    #player spotted you

    #choices
    "wander": "The player is not in sight, do you wander UP, DOWN, LEFT, RIGHT, or do you WAIT until you see the player?",

    #conditional choices
    "investigate_noise": "You hear a noise at #NOISE_POSITION#, you are at #SELF_POSITION#. You can move one sqare, do you move UP, DOWN, LEFT or RIGHT?",
    "proximity_decision": "You are #PLAYER_DISTANCE#, do you try to SNEAK closer to see the player, HIDE until you can see the player, or CHARGE at them to catch them?",
    "attack_decision": "You are #PLAYER_DISTANCE#, the player #TARGET_LOOK_SELF_STATE#, do you SNEAK after the player and quietly follow them, or do you JUMP at the player to win?",  
}

def init_command_structure():
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