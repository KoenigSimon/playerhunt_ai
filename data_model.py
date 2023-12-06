class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    def parse(self, s:str):
        self.x, self.y, self.z = map(float, s.strip('[]').split(";"))
    def __init__(self) -> None:
        self.x = self.y = self.z = 0.0
    def __str__(self) -> str:
        return f"[{str(self.x)};{str(self.y)};{str(self.z)}]"
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
        return f"[{str(self.x)};{str(self.y)}]"
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
    # config data -> to game
    action_state: int = 0       # output for debug
    # config data <- from game
    restart: bool = False       # input for restart
    gpt_model_tier: int = 0     # 0: gpt 3 turbo / 1: gpt 4 turbo
    lookat_direct: float = 0.84 # input for agent fov
    lookat_periph: float = 0.5  # input for agent fov
    distance_near: float = 5.0  # input for distance
    distance_mid: float = 10.0  # input for distance
    distance_far: float = 20.0  # input for distance

    # base data
    target_pos: Vector3
    self_pos: Vector3
    play_area: Vector2 # x,y amount columns/rows
    cell_size: Vector2 # x,y size per grid cell
    target_heading: Vector3
    self_heading: Vector3

    # action data 
    noise_position: Vector3

    def __init__(self) -> None:
        self.target_pos = Vector3()
        self.self_pos = Vector3()
        self.play_area = Vector2()
        self.cell_size = Vector2()
        self.target_heading = Vector3()
        self.self_heading = Vector3()
        self.noise_position = Vector3()

#global variables
game_data: GameData
messages: any