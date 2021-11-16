from colors import *

# Desenha os tiles do mapa
def draw_tile(graph, id, style, width):
    r = ""

    if id in graph.solid_ground:
        r = blue + '#' * width + reset
    if id in graph.rocky_ground:
        r = green + '°' * width + reset
    if id in graph.sandy_ground:
        r = yellow_bg + '▄' * width + reset
    if id in graph.marsh_ground:
        r = red + '█' * width + reset

    # Escreve a função de custo das posições pelas quais o agente passará
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1:
            r = ">"
        if x2 == x1 - 1:
            r = "<"
        if y2 == y1 + 1:
            r = "v"
        if y2 == y1 - 1:
            r = "^"

    if 'start' in style and id == style['start']:
        r = "☻"
    if 'goal' in style and id == style['goal']:
        r = "♦"
    if id in graph.rewards:
        r = '$'
    if 'number' in style and id in style['number']:
        r = "%d" % style['number'][id]
    if 'path' in style and id in style['path']:
        r = "☺"
        if(id in graph.rewards):
            graph.rewards.remove(id)
    if id in graph.walls:
        r = "▒" * width
    return r

# Desenha o mapa, substituindo espaços vazios pelos símbolos que representam os elementos necessários
def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width %
                  draw_tile(graph, (x, y), style, width), end="")
        print()
