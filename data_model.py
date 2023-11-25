class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    def parse(self, s:str):
        self.x, self.y, self.z = map(float, s.strip('[]').split(";"))
    def __init__(self) -> None:
        self.x = self.y = self.z = 0.0
    def __str__(self) -> str:
        return str(self.x) + " " + str(self.y) + " " + str(self.z)
    def __eq__(self, __value: object) -> bool:
        if self.x == self.y == self.z == __value: return True
        else: return False

class Vector2:
    x: float = 0.0
    y: float = 0.0
    def parse(self, s:str):
        self.x, self.y = map(float, s.strip('[]').split(";"))
    def __init__(self) -> None:
        self.x = self.y = 0.0
    def __str__(self) -> str:
        return str(self.x) + " " + str(self.y)
    def __eq__(self, __value: object) -> bool:
        if self.x == self.y == __value: return True
        else: return False

class Vector3_List:
    vectors = []
    def parse_append(self, s:str):
        self.vectors.append(Vector3.parse(s))
    def __init__(self) -> None:
        self.vectors = []
    def __str__(self) -> str:
        string = ""
        for vec in self.vectors:
            str(vec.x) + " " + str(vec.y) + " " + str(vec.z) + "\n"  
        return string
    pass

class GameData:
    # base data
    player_pos: Vector3
    self_pos: Vector3
    play_area: Vector2 # x,y amount columns/rows
    cell_size: Vector2 # x,y size per grid cell
    player_heading: Vector3
    self_heading: Vector3

    # action data 
    noise_position: Vector3

    def __init__(self) -> None:
        self.player_pos = Vector3()
        self.self_pos = Vector3()
        self.play_area = Vector2()
        self.cell_size = Vector2()
        self.player_heading = Vector3()
        self.self_heading = Vector3()
        self.noise_position = Vector3()

#global variables
game_data: GameData
messages: any