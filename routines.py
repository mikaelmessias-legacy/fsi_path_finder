import search
import utils
import colors
from draw import *
from grid import *

def start_search(graph, start, goal, selected_algorithm):
    came_from, evaluation, stored_nodes = {}, {}, 0

    if (selected_algorithm == 1):
        came_from, evaluation, stored_nodes = search.breadth_first(
            graph, start, goal
        )
    # if (selected_algorithm == 2):
    #     came_from, evaluation, stored_nodes = search.depth_first(
    #         graph, start, goal
    #     )
    if (selected_algorithm == 4):
        came_from, evaluation, stored_nodes = search.a_star(
            graph, start, goal
        )

    path, found = utils.graph_reconstruct_path(
        came_from, start=start, goal=goal
    )

    after_search_drawing(graph, came_from, start, goal, evaluation, path)

    if(found == False):
        print("Não existe caminho possível para esse destino.\n")
    else:
        after_search_report(stored_nodes, path, evaluation, graph.rewards, selected_algorithm)

def after_search_drawing(graph, came_from, start, goal, evaluation, path):
    # Desenha o mapa apontando o caminho do objetivo para o estado inicial do agente
    draw_grid(graph, width=3, point_to=came_from, start=start, goal=goal)
    print()

    # Desenha o mapa com o valor da função de avaliação para cada passo estudado pelo agente
    draw_grid(graph, width=4, number=evaluation, start=start, goal=goal)
    print()

    # Desenha o mapa apontando o caminho escolhido pelo agente
    draw_grid(graph, width=3, path=path)

def after_search_report(stored_nodes, path, evaluation, rewards, selected_algorithm):
    total_rewards = Grid.REWARDS.value - len(rewards)

    print(
        "\nRecompensas do agente: ",
        total_rewards,
        "\nRecompensa total em dinheiro: R$",
        (total_rewards * 12.5),
        "\n"
    )

    printReport = input("Exibir relatório de pesquisa? (s/n)\n: ")

    if printReport == 's':
        algorithm_name = 'busca em largura'
        
        if selected_algorithm == 2:
            algorithm_name = 'busca em profundidade'
        elif selected_algorithm == 3:
            algorithm_name = 'gulosa'
        elif selected_algorithm == 4:
            algorithm_name = 'A*'

        print(
            "\n> Algoritmo", algorithm_name, "\nNós armazenados: {}" .format(stored_nodes)
        )

        if selected_algorithm > 2:
            print("\nFunção de avaliação F(n) = g(n) + h(n)\n")
            for i in range(0, Grid.WIDTH.value):
                for j in range(0, Grid.HEIGHT.value):
                    point = (i, j)
                    eval_value = evaluation.get(point)

                    if(point in path):
                        print("f(({0},{1})) = {2}" .format(i, j, eval_value))

    input("\n\n" + colors.yellow + "Digite ENTER para continuar...\n\n\n" + colors.reset)