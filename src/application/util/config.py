class Config:
    """
    Classe estática que contém as configurações de cada cenário de teste
    """

    # Número de execuções para cada método de busca
    n_executions = 10

    # Seed para manter reproduzível a geração de obstáculos
    seed = 42

    # Porcentagem máxima de obstáculos no labirinto
    obstacles_percentage = 0.25

    # Variações de dimensões do labirinto quadrado (em linhas e colunas)
    maze_sizes = [50, 100, 200, 300]
