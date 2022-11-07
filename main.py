import colors
import routines
import utils
import search
from draw import *
from grid import *
from constants import *

if __name__ == '__main__':
    grid_map = grid_init()

    # Estados inicial e objetivo do agente, respectivamente
    start, goal = (Agent.INITIAL_X.value, Agent.INITIAL_Y.value), (0, 0)
    draw_grid(grid_map, width=2, start=start, goal=(0, 0))

    print(
        "\n───────────────────────────\n  Legenda:" +
        "\n───────────────────────────\n" +
        "▒ - Paredes\n" +
        colors.blue + "#" + colors.reset + " - Terreno sólido e plano\tCusto: +1\n" +
        colors.yellow_bg + "▄" + colors.reset + " - Terreno arenoso\t\tCusto: +4\n" +
        colors.green + "°" + colors.reset + " - Terreno rochoso\t\tCusto: +10\n" +
        colors.red + "█" + colors.reset + " - Terreno pantanoso\t\tCusto: +20\n\n" +
        "☻ - Posição inicial do agente\n" +
        "☺ - Demarca o caminho percorrido pelo agente\n\n" +
        "♦ - Objetivo\n" +
        "$ - Recompensas\t\t\tCusto: 0, Ganho: +12.5\n"
    )

    print(
        "Posição inicial do agente (X,Y): {0}, {1}"
        .format(Agent.INITIAL_X.value, Agent.INITIAL_Y.value),
        "\n"
    )

    x = -1
    y = -1
    validState, out_of_bounds = False, False

    while not validState:
        x = int(input("Digite a coordenada de destino X: "))
        y = int(input("Digite a coordenada de destino Y: "))

        validState, out_of_bounds = grid_map.validate_state((x, y))

        if(not validState):
            if(out_of_bounds):
                print("\n>> Coordenadas inválidas...\n")
            else:
                print("\n>> Cuidado com as paredes...\n")
    print()

    goal = (x, y)

    typed_option = -1

    while typed_option != 6:
        typed_option = -1
        validChoice = False

        while not validChoice:
            typed_option = int(input(
                "─────────────────────────────────────────────────\n" +
                colors.blue +
                "  Digite o código do algoritmo a ser executado:" +
                colors.reset +
                "\n─────────────────────────────────────────────────\n" +
                colors.yellow +
                "1. Busca em largura / breadth-first search\n" +
                colors.red +
                "2. Busca em profundidade / depth-first search\n" +
                "3. Busca gulosa / greedy search\n" +
                colors.yellow +
                "4. Busca A* / A* search\n" +
                "5. Alterar coordenadas de destino\n" +
                "6. Sair\n" +
                colors.reset +
                "\n: "
            ))

            if typed_option in {1,4,5,6}:
                validChoice = True
            elif typed_option in {2,3}:
                print("\n>> ATENÇÃO: Algoritmo não implementado\n")
                input(
                    colors.yellow +
                    "Pressione ENTER para continuar...\n\n\n" +
                    colors.reset
                )
            else:
                print("\n>> ATENÇÃO: Opção inválida\n")
                input(colors.yellow + "Pressione ENTER para continuar...\n\n\n" + colors.reset)
                continue
        
        if validChoice:
            if typed_option == 5:
                validState = False

                while not validState:
                    x = int(input("\n\nDigite a coordenada de destino X: "))
                    y = int(input("Digite a coordenada de destino Y: "))

                    validState, out_of_bounds = grid_map.validate_state((x, y))

                    if(not validState):
                        if(out_of_bounds):
                            print("\n>> Coordenadas inválidas...\n")
                        else:
                            print("\n>> Cuidado com as paredes...\n")
                print()
            elif typed_option == 6:
                break
            else:
                routines.start_search(grid_map, start, goal, typed_option)
