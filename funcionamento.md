# Funcionamento do Projeto

## Funcionamento da Leitura do Arquivo de Texto e Geração de um Grafo:

Para fazer funcionar a busca e geração desse grafo por um arquivo de texto, primeiro é necessário entender quais dados esse arquivo conterá:

- `<número de nós do grafo>`: A primeira linha conterá o número esperado de nós do grafo, no formato `int`;

- `<nó> <latitude> <longitude>`: As linhas seguintes apresentam 3 informações, as quais definem, cada linha, um nodo desse grafo, com um *id* no formato `int`, uma *latitude* e uma *longitude*, ambas do formato `float`;

- `<número de arestas do grafo>`: Essa linha quebra a sequência anterior, apresentando o número esperado de arestas do grafo, também no formato `int`;

- `<nó> <nó> <custo_da_aresta>`: As próximas e últimas linhas contém a definição das arestas do grafo, também no formato de 3 informações separadas por espaço em cada linha, para cada linha representando uma aresta do grafo; nesse caso, as 2 primeiras informações são os *ids* dos 2 nodos ligados pela aresta (lembrando que os ids são do formato `int`), já o último valor se refere ao *custo* para atravessar essa aresta, no formato `float`.

Para a linha com os nodos, criar um armazenamento temporário dos nodos, e para cada nodo, criar um objeto Nodo para ele e inserir na lista, que depois será usada para criar um objeto Grafo.

Para a linha com as arestas, isolar os *ids* e tentar buscar como chaves no grafo para retornar um nodo, e para esses nodos, criar uma aresta e adicionar essas arestas como arestas dos nodos.

Para gerar esses objetos, serão usados uma classe para cada que permite conter cada um dos dados necessários para o funcionamento delas:

### Grafos:

Os grafos precisam conter 2 variáveis de validação: *nmrArestas* e *nmrNodos*; a primeira é responsável por servir de limite máximo e mínimo para o número de nodos contidos nesse grafo, enquanto a segunda funciona como limite desse mesmo tipo, mas para as arestas desse grafo. As maioria das funções que ocorrem dentro de grafos serão invocadas a partir de um objeto deste tipo, por conveniência e por padrões impostos nos documentos fornecidos pelo professor.

*Métodos dos Grafos:*

- `vizinhos(self, nodo):` Esse método permite identificar dentro do grafo referenciado, quais são os vizinhos do nodo passado como argumento. Para fazer isso, será feita a tentativa de acessar o dicionário contendo as arestas para esse nodo passado, e então retornar uma
lista que conterá os segundos ids de cada uma dessas arestas, visando diminuir o tempo de acesso dessas informações;

- `veirifcaVizinho(self, nodo1, nodo2):` Esse método retorna um tipo `bool` que verifica se os dois nodos passados como argumento são vizinhos.

- `cost(self, nodo1, nodo2)`: Esse método fará uma verificação se os nodos passados são vizinhos, e se forem, ele acessa as arestas do nodo1, e procura por uma chave igual ao nodo2, e se houver, retorna o valor dela, que será o custo.

*Métodos dos Nodos:*

- `__eq__(self, id):` Esse método é necessário para verificar se um valor de nodo está presente em alguma estrutura de dados que contenha nodos, sendo um dos dunder methos do Python.

- `hash(self):`

*Métodos das Arestas:*
