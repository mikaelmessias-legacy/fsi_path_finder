from enum import Enum

# definir WIDTH e HEIGHT sempre no formato NxN (mesmo valor para ambos)
class Grid(Enum):
    WIDTH = 20
    HEIGHT = 20
    REWARDS = 100

# AGENT RELATED CONSTANTS
class Agent(Enum):
    INITIAL_X = 14
    INITIAL_Y = 3
