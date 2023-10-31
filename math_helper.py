import data_structs as data
import math

def distance(a: data.Vector3, b: data.Vector3):
    return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2)+math.pow(a.z-a.z,2))
def distance(a: data.Vector2, b: data.Vector2):
    return math.sqrt(math.pow(a.x-b.x,2)+math.pow(a.y-b.y,2))

def magnitude(vector: data.Vector3):
    return math.sqrt(math.pow(vector.x, 2)+math.pow(vector.y, 2)+math.pow(vector.z, 2))
def magnitude(vector: data.Vector2):
    return math.sqrt(math.pow(vector.x, 2)+math.pow(vector.y, 2))