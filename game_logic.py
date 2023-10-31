import data_structs as data

def init_game():
    global game_data
    game_data = data.GameData()

def props(cls):   
  return [i for i in cls.__dict__.keys() if i[:1] != '_']

#message supports only one field per message, keep that in mind
def parse_input_data(message: str):
    for name in props(game_data):
        if message.startswith(name):
            raw_data = message.removeprefix(name).strip()
            game_data.__getattribute__(name).parse(raw_data)
            pass

def validate_action(action):
    pass

#test
if __name__ == '__main__':
    init_game()
    message = "player_pos 1.2,3.4,5.6"
    parse_input_data(message)
    message = "play_area 3.4,5.6"
    parse_input_data(message)
    message = "player_heading 1.2,3.4,5.6"
    parse_input_data(message)
    #game_data.player_pos.parse(message)
    print( game_data.player_pos)
    print( game_data.play_area)
    print( game_data.player_heading)