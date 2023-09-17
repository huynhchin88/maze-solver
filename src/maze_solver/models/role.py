#six unique roles you can assign to the squares in any given maze:
#1.Enemy, 2.Entrance, 3.Exit, 4.Exterior, 5.Reward, 6.Wall

from enum import IntEnum, auto

class Role(IntEnum):
    #design pattern: null object pattern = have a 'dedicated null object' representing the null value of the class
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()