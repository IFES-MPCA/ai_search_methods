# IA - Métodos de busca

## Algoritmos

### DFS

### UCS

### A*

Resultados com execução de labirinto 100x100:
| método                        | média (ms) | desvio (ms) | desvio (%) | custo caminho | nós gerados | nós expandidos |
|-------------------------------|------------|-------------|------------|---------------|-------------|----------------|
| BreadthFirstSearch            | 152.00     | 14.85       | 9.77       | 110           | 7785        | 7785           |
| DepthFirstSearch              | 2.03       | 5.25        | 258.84     | 137           | 417         | 141            |
| UniformCostSearch             | 360.45     | 13.64       | 3.78       | 110           | 7785        | 7785           |
| AStar (Heurística Manhattan)  | 12.50      | 6.26        | 50.12      | 114           | 414         | 128            |
| AStar (Heurística Euclidiana) | 76.05      | 7.84        | 10.31      | 112           | 1809        | 1453           |

Resultados com execução de labirinto 200x200:
| método                        | média (ms) | desvio (ms) | desvio (%) | custo caminho | nós gerados | nós expandidos |
|-------------------------------|------------|-------------|------------|---------------|-------------|----------------|
| BreadthFirstSearch            | 691.73     | 27.38       | 3.96       | 222           | 31195       | 31195          |
| DepthFirstSearch              | 723.74     | 57.89       | 8.00       | 239           | 12492       | 11909          |
| UniformCostSearch             | 2621.36    | 245.35      | 9.36       | 222           | 31195       | 31195          |
| AStar (Heurística Manhattan)  | 47.14      | 4.94        | 10.47      | 231           | 804         | 253            |
| AStar (Heurística Euclidiana) | 504.64     | 30.11       | 5.97       | 226           | 7633        | 6931           |

Resultados com execução de labirinto 300x300:
| método                        | média (ms) | desvio (ms) | desvio (%) | custo caminho | nós gerados | nós expandidos |
|-------------------------------|------------|-------------|------------|---------------|-------------|----------------|
| BreadthFirstSearch            | 1695.47    | 113.13      | 6.67       | 323           | 70147       | 70147          |
| DepthFirstSearch              | 8.94       | 5.54        | 62.01      | 376           | 1264        | 383            |
| UniformCostSearch             | 8664.45    | 511.64      | 5.91       | 323           | 70147       | 70147          |
| AStar (Heurística Manhattan)  | 115.81     | 7.26        | 6.27       | 337           | 1298        | 416            |
| AStar (Heurística Euclidiana) | 1232.12    | 74.42       | 6.04       | 329           | 14270       | 13170          |

## Experimentos

### Configuração da máquina

#### Software

- Windows 10
- Python 3.8

#### Hardware

- Notebook Acer Aspire Nitro 5
- Modelo: [AN515-54-718D](https://quenotebookcomprar.com.br/acer-nitro-5-an515-54-718d)
- 16GB RAM DDR4
- SSD 256GB

Processador:
- Intel® Core™ [i7-9750H](https://ark.intel.com/content/www/br/pt/ark/products/191045/intel-core-i79750h-processor-12m-cache-up-to-4-50-ghz.html) 9ª Geração
- 6 núcleos, 12 threads
- Frequência máxima de  4.50 GHz e base de 2.60 GHz

## Resultados
