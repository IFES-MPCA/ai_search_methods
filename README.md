# IA - Métodos de busca

**Aluno:** Antônio Carlos Durães da Silva

## Algoritmos

Com exceção do A*, todos são métodos de busca não informada, isto é, não contam com uma heurística para
orientar/direcionar a busca de um estado específico até o objetivo.

Sobre otimalidade, dado que o nosso problema tem custos distintos de movimentação, apenas algoritmos (A* e UCS) com
heurísticas que consideram os custos podem ser ótimos. O BFS encontra o
caminho ótimo para problemas em que as ações tenham mesmo custo (não é o caso).

Os algoritmos compartilham boa parte da implementação, a principal variação se dá nas estruturas de dados utilizadas,
como fila (para o BFS), pilha (para o DFS) e fila de prioridade (para UCS e A*).

### Breadth-First Search (BFS)

Dado um nó inicial ("X", por exemplo), o BFS explora todos os seus vizinhos até encontrar o estado objetivo. Para cada
vizinho verificado, seus vizinhos são adicionados à fila para repetirem o processo. Seu comportamento se resume a uma
busca exaustiva.

<img src="assets\bfs.gif" width="150"/>

### Depth-First Search (DFS)

Dado um nó inicial ("X", por exemplo), o DFS explora todo o ramo até encontrar o estado objetivo ou até findar o ramo
(encontrar um nó folha, sem filhos). Caso finde o ramo sem encontrar o objetivo, o DFS retrocede e
explora os ramos dos nós vizinhos do nó expandido anteriormente ("X").

<img src="assets\dfs.gif" width="150"/>

### Uniform-Cost Search (UCS)

O UCS pode ser visto como uma extensão do BFS. Ao invés de expandir todos os nós vizinhos de um nó, o UCS prioriza os
nós com menor custo g, além de verificar se é possível melhorar o caminho até um nó já visto, desde que esse caminho
seja menos custoso.

<img src="assets\ucs.gif" width="150"/>

### A* (A Star)

O diferencial deste algoritmo é que ele considera não só o custo g (nó atual até o nó objetivo) mas também o custo h
(estado atual até o objetivo), entregue por uma heurística. Por esse diferencial, o A* mescla velocidade de execução com
o encontro de um caminho ótimo.

Heurística de distância octil:

<img src="assets\a_star_octil.gif" width="150"/>

Heurística de distância euclidiana:

<img src="assets\a_star_euclidian.gif" width="150"/>

## Experimentos

Para acelerar a execução dos métodos de buscas, algumas decisões de implementação foram feitas:

- Utilizar conjuntos ("set") para fronteira e visitados para aproximar
  a checagem à complexidade [O(1)](https://wiki.python.org/moin/TimeComplexity#:~:text=notes-,x%20in%20s,-O(1))
- Avançar com loop se o nó já estiver na fronteira ou visitado

Foram realizadas **100 execuções** para cada algoritmo, todas com a mesma **semente (42)**.

Os números de pontos flutuantes são arredondados para duas casas decimais somente no momento de gerar a tabela
apresentada na seção de resultados.

### Métricas

#### Tempo de execução

Para mensurar tempo de execução foram utilizados a média aritmética e o desvio padrão populacional. A
mensuração do tempo só inicia ao invocar o método de busca, portanto, etapas como criação do mapa e escrita dos
resultados em arquivos não são inclusas nessa medição.

#### Tamanho e custo do caminho final

O tamanho e custo do caminho final incluem o nó inicial e o nó objetivo, isto é, foi considerado o caminho completo.

#### Número de nós gerados e expandidos

O número de nós gerados foi tomado como o número remanescentes na fronteira quando o algoritmo terminou. Já o número de
expandidos como foi tomado como o número de nós visitados. Ambas as métricas foram replicadas pelo que pode ser
observado no código dado como exemplo (template).

### Expectativas

É esperado que algoritmos não ótimos, como o DFS, executem mais rápido ao custo de encontrarem um caminho mais custoso.
Espera-se também o oposto, isto é, que métodos ótimos, como UCS, executem mais lentamente (por explorar mais nós) ao
custo de encontrarem um
caminho mais barato.

Além da otimalidade, espera-se que o uso de heurística também seja um fator impactante no tempo de execução, tendo em
vista adição de processamento para cálculos aritméticos e verificações adicionais.

### Configuração da máquina

#### Software

Testes executados com Python 3.8 e Windows 10.

#### Hardware

- Notebook Acer Aspire Nitro 5, modelo [AN515-54-718D](https://quenotebookcomprar.com.br/acer-nitro-5-an515-54-718d)
- 16GB RAM DDR4
- SSD 256GB

Processador:

- Intel®
  Core™ [i7-9750H](https://ark.intel.com/content/www/br/pt/ark/products/191045/intel-core-i79750h-processor-12m-cache-up-to-4-50-ghz.html)
  9ª Geração
- 6 núcleos, 12 threads
- Frequência máxima de 4.50 GHz e base de 2.60 GHz

## Resultados

### Cenário 1: Labirinto 200x200

| método                    | média (ms) | desvio (ms) | desvio (%) | custo caminho | tamanho caminho | nós gerados | nós expandidos |
|---------------------------|------------|-------------|------------|---------------|-----------------|-------------|----------------|
| Depth First Search (DFS)  | 727.82     | 44.04       | 6.05       | 313.39        | 239             | 583         | 11909          |
| Breath First Search (BFS) | 691.91     | 35.34       | 5.11       | 297.63        | 222             | 0           | 31195          |
| Uniform Cost Search (UCS) | 2420.63    | 74.02       | 3.06       | 295.14        | 222             | 0           | 31195          |
| A* (Octile)               | 196.04     | 9.66        | 4.93       | 295.73        | 223             | 748         | 3956           |
| A* (Euclidian)            | 346.74     | 16.44       | 4.74       | 295.14        | 222             | 792         | 7996           |

Por não contar com heurística, o DFS apresenta o caminho mais custoso, tal algoritmo é ideal para encontrar rapidamente
alguma solução, sem se preocupar com heurística ou otimalidade. Sua velocidade e número de nós expandidos irão
depender do cenário testado, como será mostrado no próximo caso de teste.

Se ainda não há heurística, mas é desejável priorizar um caminho mais curto ou ótimo (caso não haja distinção de custo
entre as ações) sobre o tempo de execução, o BFS é o algoritmo ideal. O algoritmo foi o terceiro mais lento e com alto
número de nós expandidos, trazendo maior consumo de memória assim como o UCS. Embora a solução encontrada seja
satisfatória, não foi possível encontrar a ótima, pois o problema admite ações de custos distintos.

O UCS é uma boa opção quando há a necessidade da solução ótima, uma forma de calcular o custo g (custo do nó inicial
até um nó específico), mas não há uma heurística admissível para o problema. O algoritmo foi o mais lento (cerca de
3.3 vezes mais lento que o DFS), o que era esperado, pois, além de expandir muitos nós, também inclui o tempo para
calcular o custo dos caminhos gerados até encontrar a solução.

De posse de uma heurística, A* é o método recomendado quando o objetivo for combinar a otimalidade da solução com a
velocidade de execução, ambas características vão depender da heurística utilizada. Quando usada a heurística
euclidiana, por ser admissível (não superestima o custo de atingir o objetivo), o algoritmo gera uma solução ótima. Em
contrapartida, ao utilizar a [distância octil](https://www.sciencedirect.com/science/article/pii/S1000936116301182)
como heurística, o algoritmo executa 1.76 vezes mais rápido que a versão euclidiana, mas gera uma solução não ótima,
embora próxima dela.

### Cenário 2: Labirinto 300x300

| método              | média (ms) | desvio (ms) | desvio (%) | custo caminho | tamanho caminho | nós gerados | nós expandidos |
|---------------------|------------|-------------|------------|---------------|-----------------|-------------|----------------|
| Uniform Cost Search | 7422.34    | 162.06      | 2.18       | 436.32        | 323             | 0           | 70147          |
| A* (Euclidian)      | 549.68     | 25.93       | 4.72       | 436.32        | 323             | 1253        | 12722          |
| A* (Octile)         | 267.16     | 26.16       | 9.79       | 436.32        | 323             | 923         | 5684           |
| Breath First Search | 1607.40    | 57.92       | 3.60       | 439.64        | 323             | 0           | 70147          |
| Depth First Search  | 8.28       | 9.51        | 114.81     | 495.54        | 376             | 881         | 383            |

Neste cenário, o DFS segue apresentando o caminho mais custoso, contudo tira proveito da posição do nó
objetivo e seu comportamento simples de expansão para gerar a resposta mais rápida. Seu desvio padrão é alto, pois
sua execução é extremamente rápida.

Já o BFS, foi o segundo mais lento e com maior número de nós expandidos, ao lado do UCS. Embora tenha encontrado um
caminho de mesmo comprimento que o ótimo, o custo ainda foi superior por não ter priorizado alguma célula diagonal.

A busca de custo uniforme manteve-se como a menos rápida, dessa vez sendo cerca de 4.61 vezes mais lenta que o segundo
algoritmo mais demorado (BFS).

Diferente do cenário anterior, ao utilizar a distância octil, o A* além de executar com menos da metade do tempo da
versão euclidiana, também conseguiu encontrar uma solução ótima (para esse labirinto em específico). Sua versão
euclidiana executou abaixo de 600ms, contudo expandiu mais do que o dobro de nós.

## Organização do código

```
src
│
└─── application
│   │
│   └─── report
│   └─── util
│
└─── models
│   │
│   └─── problem
│   │   │
│   │   └─── maze_2d
│   │
│   └─── search
│       │
│       └─── methods
│   
└─── results
└─── ui
```

- **application/report:** Utilitários para escrever a saída dos resultados
- **application/util:** Classe com as configurações (seed, tamanho, porcentagem de obstáculos) dos cenários e utilitário
  para mensura tempo de execução de uma função


- **search:** Contém classes genéricas que especificam a assinatura dos métodos de busca e heurística, além das
  implementações dos métodos de busca
- **search/methods:** Classes que implementam os métodos de busca (Uniform Cost Search, A*, Breath First Search, Depth
  First Search)


- **results:** Diretório onde serão armazenados os arquivos CSV de resultados
- **ui:** Diretório que contém código para visualização gráfica dos algoritmos

Como optei por separar os métodos de busca do problema a ser resolvido, houve a necessidade de criar um diretório com
modelos e funções relacionadas ao problema do labirinto:

- **models/problem/maze_2d:** Modelos como célula / bloco, heurísticas para distância, modelo do próprio problema e uma
  classe para representar o labirinto em si
- **models/problem:** Modelo genérico de problema (não se limita a labirinto) e modelos específicos para o labirinto
