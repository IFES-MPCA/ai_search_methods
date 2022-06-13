# IA - Métodos de busca

## Algoritmos

### Breadth-First Search (BFS)

Dado um nó inicial ("X", por exemplo), o BFS explora todos os seus vizinhos até encontrar o estado objetivo. Para cada
vizinho verificado, seus vizinhos são adicionados à fila para repetirem o processo. Seu comportamento se resume a uma
busca exaustiva.

### Depth-First Search (DFS)

Dado um nó inicial ("X", por exemplo), o DFS explora todo o ramo até encontrar o estado objetivo ou até findar o ramo
(encontrar um nó folha, sem filhos). Caso finde o ramo sem encontrar o objetivo, o DFS retrocede e
explora os ramos dos nós vizinhos do nó expandido anteriormente ("X").

### Uniform-Cost Search (UCS)

O UCS pode ser visto como uma extensão do BFS. Ao invés de expandir todos os nós vizinhos de um nó, o UCS prioriza os
nós com menor custo g, para isso é comumente implementado com uma fila de prioridade.

### A* (A Star)

O diferencial deste algoritmo é que ele considera não só o custo g (nó atual até o nó objetivo) mas também o custo h
(estado atual até o objetivo), entregue por uma heurística. Por esse diferencial, o A* mescla velocidade de execução com
o encontro de um caminho ótimo.

## Características

Com exceção do A*, todos são métodos de busca **não informada**, isto é, não contam com uma heurística para
orientar/direcionar a busca de um estado específico até o objetivo.

Sobre **otimalidade**, dado que o nosso problema tem custos distintos de movimentação (permite movimentar-se nas
diagonais), apenas algoritmos (A* e UCS) com heurísticas que consideram os custos podem ser ótimos. O BFS encontra o
caminho ótimo para problemas em que as ações tenham mesmo custo (não é o caso).

## Experimentos

Para acelerar a execução dos métodos de buscas, algumas decisões de implementação foram feitas:

- Utilizar conjuntos ("set") para fronteira e visitados para aproximar
  a checagem à complexidade [O(1)](https://wiki.python.org/moin/TimeComplexity#:~:text=notes-,x%20in%20s,-O(1))
- Avançar com loop se o nó já estiver na fronteira ou visitado

Foram realizadas **100 execuções** para cada algoritmo para ser possível ter medidas consistentes para **média** e **
desvio
padrão** do tempo de execução. A mesma **semente (42)** foi utilizada para todas as execuções.

A mensuração do tempo só inicia ao invocar o método de busca. Etapas como criação do mapa e escrita dos resultados em
arquivos não são inclusas nessa medição.

### Expectativas

É esperado que algoritmos não ótimos, como o DFS, executem mais rápido ao custo de encontrarem um caminho mais custoso.
Espera-se também o oposto, isto é, que métodos ótimos, como UCS, executem mais lentamente ao custo de encontrarem um
caminho mais barato.

Além da otimalidade, espera-se que o uso de heurística também seja um fator impactante no tempo de execução, tendo em
vista adição de processamento para cálculos aritméticos e verificações adicionais.

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

- Intel®
  Core™ [i7-9750H](https://ark.intel.com/content/www/br/pt/ark/products/191045/intel-core-i79750h-processor-12m-cache-up-to-4-50-ghz.html)
  9ª Geração
- 6 núcleos, 12 threads
- Frequência máxima de 4.50 GHz e base de 2.60 GHz

## Resultados

Resultados com execução de labirinto 300x300:

| método              | média (ms) | desvio (ms) | desvio (%) | custo caminho | tamanho caminho | nós gerados | nós expandidos |
|---------------------|------------|-------------|------------|---------------|-----------------|-------------|----------------|
| Uniform Cost Search | 7976.46    | 306.51      | 3.84       | 436.32        | 323             | 70147       | 70147          |
| Breath First Search | 1685.56    | 120.11      | 7.13       | 439.64        | 323             | 70147       | 70147          |
| A* (Euclidian)      | 1243.84    | 70.34       | 5.66       | 441.49        | 329             | 14270       | 13170          |
| A* (Manhattan)      | 112.43     | 19.47       | 17.31      | 449.49        | 337             | 1298        | 416            |
| Depth First Search  | 8.44       | 8.96        | 106.19     | 495.54        | 376             | 1264        | 383            |
