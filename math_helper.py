import data_model as data
import math

def distance(a: data.Vector3, b: data.Vector3):
    return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2)+math.pow(a.z-a.z,2))
def distance(a: data.Vector2, b: data.Vector2):
    return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2))

def magnitude(vector: data.Vector3):
    return math.sqrt(math.pow(vector.x, 2)+math.pow(vector.y, 2)+math.pow(vector.z, 2))
def magnitude(vector: data.Vector2):
    return math.sqrt(math.pow(vector.x, 2)+math.pow(vector.y, 2))

def position_to_grid(position: data.Vector3, cell_size: data.Vector2) -> tuple:
    #currently center aligned
    if cell_size.x == 0 or cell_size.y == 0: return (-1, -1)
    grid_pos_x = round(position.x / cell_size.x)
    grid_pos_y = round(position.z / cell_size.y)
    # TODO: out of bounds check via play area
    return (grid_pos_x, grid_pos_y)

def look_at_factor(self_heading: data.Vector3, target_heading: data.Vector3) -> float:
    self_heading = self_heading % 360
    target_heading = target_heading % 360
    diff = abs(self_heading - target_heading)
    if diff > 180:
        diff = 360 - diff
    similarity = 1 - (diff / 180)
    return similarity

def heading_angle(vec: data.Vector3):
    angle_rad = math.atan2(vec.y, vec.x)
    angle_deg = math.degrees(angle_rad)
    if angle_deg < 0:
        angle_deg += 360
    return angle_deg