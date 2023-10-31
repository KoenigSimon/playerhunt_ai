from dataclasses import dataclass

@dataclass
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

class Vector2:
    x: float = 0.0
    y: float = 0.0

@dataclass
class GameData:
    player_pos: Vector3
    self_pos: Vector3
    play_area: Vector2
    #player heading
    #self heading
