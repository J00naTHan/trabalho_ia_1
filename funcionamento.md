# Funcionamento do Projeto

## Funcionamento da Leitura do Arquivo de Texto e Geração de um Grafo:

Para fazer funcionar a busca e geração desse grafo por um arquivo de texto, primeiro é necessário entender quais dados esse arquivo conterá:

- `<número de nós do grafo>`: A primeira linha conterá o número esperado de nós do grafo, no formato `int`;

- `<nó> <latitude> <longitude>`: As linhas seguintes apresentam 3 informações, as quais definem, cada linha, um nodo desse grafo, com um *id* no formato `int`, uma *latitude* e uma *longitude*, ambas do formato `float`;

- `<número de arestas do grafo>`: Essa linha quebra a sequência anterior, apresentando o número esperado de arestas do grafo, também no formato `int`;

- `<nó> <nó> <custo_da_aresta>`: As próximas e últimas linhas contém a definição das arestas do grafo, também no formato de 3 informações separadas por espaço em cada linha, para cada linha representando uma aresta do grafo; nesse caso, as 2 primeiras informações são os *ids* dos 2 nodos ligados pela aresta (lembrando que os ids são do formato `int`), já o último valor se refere ao *custo* para atravessar essa aresta, no formato `float`.

Para a linha com os nodos, criar um armazenamento temporário dos nodos, e para cada nodo, criar um objeto Nodo para ele e inserir na lista, que depois será usada para criar um objeto Grafo.

Para a linha com as arestas, isolar os *ids* e tentar buscar como chaves no grafo para retornar um nodo, e para esses nodos, criar uma aresta e adicionar essas arestas como arestas dos nodos.

