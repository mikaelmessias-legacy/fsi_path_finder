from structures import Queue
from structures import PriorityQueue

# --------------------------------------------------------
# Buscas Não-Informadas
# --------------------------------------------------------

# Algoritmo de busca em largura
def breadth_first(graph, start, goal):
    frontier = Queue()
    frontier.push(start)

    came_from = {}
    came_from[start] = None

    cost_so_far = {}
    cost_so_far[start] = 0

    count = 0

    while not frontier.empty():
        current = frontier.pop()

        if current == goal:
            break

        for neighbour in graph.neighbors(current):
            if neighbour not in came_from:
                new_cost = cost_so_far[current] + graph.cost(current, neighbour)
                cost_so_far[neighbour] = new_cost
                frontier.push(neighbour)
                came_from[neighbour] = current
                count = count + 1

    return came_from, cost_so_far, count

def dfs(graph, visited, current, goal, came_from, cost):
    if current == goal:
        return

    if current not in visited:
        visited.append(current)
        for neighbour in graph.neighbors(current):
            if (current not in came_from):
                new_cost = cost[current] + graph.cost(current, neighbour)
                cost[neighbour] = new_cost

                came_from[neighbour] = current
                
                dfs(graph, visited, neighbour, goal, came_from, cost)

# Algoritmo de busca em profundidade
def depth_first(graph, start, goal):
    visited = []

    came_from = {}
    came_from[start] = None

    cost_so_far = {}
    cost_so_far[start] = 0

    dfs(graph, visited, start, goal, came_from, cost_so_far)

    return came_from, cost_so_far, len(visited)
# --------------------------------------------------------
# Buscas Informadas - Heurísticas
# --------------------------------------------------------

# A heurística é definida como a distância entre o ponto onde o agente se encontra e o ponto de destino / objetivo
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# Algoritmo de busca A*
def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.push(start, 0)
    count = 0
    came_from = {}
    cost_so_far = {}
    eval_v = {}
    came_from[start] = None
    cost_so_far[start] = 0
    eval_v[start] = 0

    while not frontier.empty():
        current = frontier.pop()

        if current == goal:
            break

        for neighbour in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, neighbour)
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic(goal, neighbour)
                eval_v[neighbour] = priority
                frontier.push(neighbour, priority)
                count = count + 1
                came_from[neighbour] = current

    return came_from, eval_v, count
