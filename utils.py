#  Busca os passos escolhidos pelo agente para atingir o objetivo
def graph_reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    found = True

    while current != start:
        if(came_from.get(current) == None):
            found = False
            break
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path, found
