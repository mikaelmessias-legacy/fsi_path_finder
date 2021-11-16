from random import randint
from graph import *

from constants import Grid, Agent

def grid_add_walls(graph, gridWidth, gridHeight):
    # Constrói as paredes do mapa
    print("- Adicionando paredes........")

    min_width, max_width = 0, gridWidth-1
    min_height, max_height = 0, gridHeight-1

    for i in range(0, gridWidth):
        graph.walls.append((i, min_width))
        graph.walls.append((i, max_width))
    for j in range(0, gridHeight):
        graph.walls.append((min_height, j))
        graph.walls.append((max_height, j))

    walls_count = 0

    while walls_count < 100:
        i = randint(0, gridWidth)
        j = randint(0, gridHeight)
        if ((i, j) != (Agent.INITIAL_X.value, Agent.INITIAL_Y.value)):
            graph.walls.append((i, j))
        walls_count = walls_count + 1


def grid_add_rewards(graph, amount, gridWidth, gridHeight):
    # Espalha as recompensas pelo mapa
    print("- Adicionando recompensas........")

    rewards_count = 0

    while rewards_count < amount:
        i = randint(0, gridWidth)
        j = randint(0, gridHeight)
        if ((i, j) not in graph.walls and (i, j) != (Agent.INITIAL_X.value, Agent.INITIAL_Y.value)):
            graph.rewards.append((i, j))
            rewards_count = rewards_count + 1


def grid_add_ground(graph, gridWidth, gridHeight):
    # Terrenos
    print("- Adicionando terrenos........")

    ground_count = {"solido": 0, "rochoso": 0, "arenoso": 0, "pantanoso": 0}
    grid_quadrant = 0
    current_type = ''
    x1, y1, x2, y2 = 0, 5, 0, 5
    i, j = 0, 0
    quadrants = gridWidth / 5
    maxQuadrants = quadrants * quadrants
    maxGroundCount = maxQuadrants / 4

    while grid_quadrant < maxQuadrants:
        current_type = randint(0, 4)

        if(current_type == 0 and ground_count["solido"] < maxGroundCount):
            current_type = "solido"
            for i in range(x1, y1):
                for j in range(x2, y2):
                    graph.solid_ground.append((i, j))
        elif(current_type == 1 and ground_count["rochoso"] < maxGroundCount):
            current_type = "rochoso"
            for i in range(x1, y1):
                for j in range(x2, y2):
                    graph.rocky_ground.append((i, j))
        elif(current_type == 2 and ground_count["arenoso"] < maxGroundCount):
            current_type = "arenoso"
            for i in range(x1, y1):
                for j in range(x2, y2):
                    graph.sandy_ground.append((i, j))
        elif(current_type == 3 and ground_count["pantanoso"] < maxGroundCount):
            current_type = "pantanoso"
            for i in range(x1, y1):
                for j in range(x2, y2):
                    graph.marsh_ground.append((i, j))
        else:
            current_type = ''

        if current_type != '':
            ground_count[current_type] = ground_count[current_type] + 1
            grid_quadrant = grid_quadrant + 1
            if x1 == gridWidth - 5 and y1 == gridHeight:
                x1 = 0
                y1 = 5
                x2 = x2 + 5
                y2 = y2 + 5
            else:
                x1 = x1 + 5
                y1 = y1 + 5
            print("\t> Quadrante %d: " % grid_quadrant + current_type)

# @param graph: Graph


def grid_add_weights(graph):
    solid_points = []
    rocky_points = []
    sandy_points = []
    marsh_points = []

    print("- Adicionando pesos........")

    for i in range(graph.width):
        for j in range(graph.height):
            id = (i, j)
            if(id not in graph.rewards):
                if(id in graph.solid_ground):
                    solid_points.append((i, j))
                elif(id in graph.rocky_ground):
                    rocky_points.append((i, j))
                elif(id in graph.sandy_ground):
                    sandy_points.append((i, j))
                elif(id in graph.marsh_ground):
                    marsh_points.append((i, j))

    weights = {}

    for loc in solid_points:
        weights[loc] = 1
    for loc in rocky_points:
        weights[loc] = 10
    for loc in sandy_points:
        weights[loc] = 4
    for loc in marsh_points:
        weights[loc] = 20
    for loc in graph.rewards:
        weights[loc] = 0

    graph.weights.update(weights)


def grid_init():
    gridWidth, gridHeight, rewardsAmount = Grid.WIDTH.value, Grid.HEIGHT.value, Grid.REWARDS.value

    grid = Graph(gridWidth, gridHeight)

    grid_add_walls(grid, gridWidth, gridHeight)
    grid_add_rewards(grid, rewardsAmount, gridWidth, gridHeight)
    grid_add_ground(grid, gridWidth, gridHeight)
    grid_add_weights(grid)
    print("\nTudo pronto!\n")

    return grid
