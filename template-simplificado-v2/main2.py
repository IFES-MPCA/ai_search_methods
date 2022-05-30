import random
from collections import deque
from math import inf, sqrt

from src.models.cell import Cell
from src.search_methods.depth_first_search import DepthFirstSearch
from viewer import MazeViewer


def gera_labirinto(n_linhas, n_colunas, inicio, goal):
    # cria labirinto vazio
    labirinto = [[0] * n_colunas for _ in range(n_linhas)]

    # adiciona células ocupadas em locais aleatórios de
    # forma que 25% do labirinto esteja ocupado
    numero_de_obstaculos = int(0.25 * n_linhas * n_colunas)
    for _ in range(numero_de_obstaculos):
        linha = random.randint(0, n_linhas - 1)
        coluna = random.randint(0, n_colunas - 1)
        labirinto[linha][coluna] = 1

    # remove eventuais obstáculos adicionados na posição
    # inicial e no goal
    labirinto[inicio.y][inicio.x] = 0
    labirinto[goal.y][goal.x] = 0

    return labirinto


class Celula:
    def __init__(self, y, x, anterior):
        self.y = y
        self.x = x
        self.anterior = anterior


def distancia(celula_1, celula_2):
    dx = celula_1.x - celula_2.x
    dy = celula_1.y - celula_2.y
    return sqrt(dx ** 2 + dy ** 2)


def esta_contido(lista, celula):
    for elemento in lista:
        if (elemento.y == celula.y) and (elemento.x == celula.x):
            return True
    return False


def custo_caminho(caminho):
    if len(caminho) == 0:
        return inf

    custo_total = 0
    for i in range(1, len(caminho)):
        custo_total += distancia(caminho[i].anterior, caminho[i])

    return custo_total


def obtem_caminho(goal):
    caminho = []

    celula_atual = goal
    while celula_atual is not None:
        caminho.append(celula_atual)
        celula_atual = celula_atual.anterior

    # o caminho foi gerado do final para o
    # começo, então precisamos inverter.
    caminho.reverse()

    return caminho


def celulas_vizinhas_livres(celula_atual, labirinto):
    # generate neighbors of the current state
    vizinhos = [
        Celula(y=celula_atual.y - 1, x=celula_atual.x - 1, anterior=celula_atual),
        Celula(y=celula_atual.y + 0, x=celula_atual.x - 1, anterior=celula_atual),
        Celula(y=celula_atual.y + 1, x=celula_atual.x - 1, anterior=celula_atual),
        Celula(y=celula_atual.y - 1, x=celula_atual.x + 0, anterior=celula_atual),
        Celula(y=celula_atual.y + 1, x=celula_atual.x + 0, anterior=celula_atual),
        Celula(y=celula_atual.y + 1, x=celula_atual.x + 1, anterior=celula_atual),
        Celula(y=celula_atual.y + 0, x=celula_atual.x + 1, anterior=celula_atual),
        Celula(y=celula_atual.y - 1, x=celula_atual.x + 1, anterior=celula_atual),
    ]

    # seleciona as células livres
    vizinhos_livres = []
    for v in vizinhos:
        # verifica se a célula esta dentro dos limites do labirinto
        if (v.y < 0) or (v.x < 0) or (v.y >= len(labirinto)) or (v.x >= len(labirinto[0])):
            continue
        # verifica se a célula esta livre de obstáculos.
        if labirinto[v.y][v.x] == 0:
            vizinhos_livres.append(v)

    return vizinhos_livres


def breadth_first_search(labirinto, inicio, goal, viewer):
    # nós gerados e que podem ser expandidos (vermelhos)
    fronteira = deque()
    # nos ja expandidos (amarelos)
    expandidos = set()

    # adiciona o no inicial na fronteira
    fronteira.append(inicio)

    # variável para armazenar o goal quando ele for encontrado.
    goal_encontrado = None

    # Repete enquanto nos não encontramos o goal e ainda
    # existem para serem expandidos na fronteira. Se
    # acabarem os nos da fronteira antes do goal ser encontrado,
    # então ele não é alcançável.
    while (len(fronteira) > 0) and (goal_encontrado is None):

        # seleciona o no mais antigo para ser expandido
        no_atual = fronteira.popleft()

        # busca os vizinhos do nó
        vizinhos = celulas_vizinhas_livres(no_atual, labirinto)

        # para cada vizinho verifica se é o goal e adiciona na
        # fronteira se ainda não foi expandido e não esta na fronteira
        for v in vizinhos:
            if v.y == goal.y and v.x == goal.x:
                goal_encontrado = v
                # encerra o loop interno
                break
            else:
                if (not esta_contido(expandidos, v)) and (not esta_contido(fronteira, v)):
                    fronteira.append(v)

        expandidos.add(no_atual)

        viewer.update(generated=fronteira,
                      expanded=expandidos)

    caminho = obtem_caminho(goal_encontrado)
    cost = custo_caminho(caminho)

    return caminho, cost


def main():
    SEED = 42  # coloque None no lugar do 42 para deixar aleatorio
    N_LINHAS = 10
    N_COLUNAS = 10
    INICIO = Celula(y=0, x=0, anterior=None)
    GOAL = Celula(y=N_LINHAS - 1, x=N_COLUNAS - 1, anterior=None)

    random.seed(SEED)

    """
    O labirinto será representado por uma matriz (lista de listas)
    em que uma posição tem 0 se ela é livre e 1, se ela está ocupada.
    """
    labirinto = gera_labirinto(N_LINHAS, N_COLUNAS, INICIO, GOAL)

    viewer = MazeViewer(labirinto, INICIO, GOAL,
                        step_time_miliseconds=100, zoom=20)

    INICIO = Cell(y=0, x=0, previous=None)
    GOAL = Cell(y=N_LINHAS - 1, x=N_COLUNAS - 1, previous=None)
    dfs = DepthFirstSearch(viewer, INICIO, GOAL)

    r = dfs.search()
    print(r.path)

    viewer.update(path=r.path)
    viewer.pause()

    print("OK!")
    return 0


if __name__ == "__main__":
    main()
