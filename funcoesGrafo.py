from grafo import Grafo, Nodo, Aresta


def adjacente(grafo, nodo1, nodo2):
  if isinstance(grafo, Grafo) and isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
    for aresta in grafo.arestas:
      if (aresta.nodo1 == nodo1 and aresta.nodo2 == nodo2) or (aresta.nodo1 == nodo2 and aresta.nodo2 == nodo1):
        return True
    return False
  raise TypeError('Grafo deve ser objeto do tipo Grafo e os nós devem ser objetos do tipo Nodo ou int')


def vizinhos(grafo, nodo):
  if isinstance(grafo, Grafo) and isinstance(nodo, Nodo):
    vizinhos = set()
    for aresta in grafo.arestas:
      if aresta.nodo1 == nodo:
        vizinhos.add(aresta.nodo2)
      elif aresta.nodo2 == nodo:
        vizinhos.add(aresta.nodo1)
    return vizinhos
  raise TypeError('Grafo deve ser objeto do tipo Grafo e o nó deve ser objeto do tipo Nodo')


def adicionarAresta(grafo, nodo1, nodo2, custo):
  if isinstance(grafo, Grafo) and isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo) and isinstance(custo, int):
    if nodo1 not in grafo.nodos:
      raise ValueError('O primeiro nodo não está no grafo')
    elif nodo2 not in grafo.nodos:
      raise ValueError('O segundo nodo não está no grafo')
    novaAresta = Aresta(nodo1, nodo2, custo)
    grafo.arestas.add(novaAresta)
    return novaAresta
  raise TypeError('Grafo deve ser objeto do tipo grafo, nó deve ser objeto do tipo Nodo e o custo deve ser do tipo int')


def removerAresta(grafo, nodo1, nodo2):
  if isinstance(grafo, Grafo) and isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
    for aresta in grafo.arestas:
      if (aresta.nodo1 == nodo1 and aresta.nodo2 == nodo2) or (aresta.nodo1 == nodo2 and aresta.nodo2 == nodo1):
        grafo.arestas.remove(aresta)
        return aresta
    raise ValueError('Aresta não existe para este grafo')
  raise TypeError('Grafo deve ser objeto do tipo grafo e os nós devem ser objetos do tipo Nodo')


def adicionarNodo(grafo, nodo):
  if isinstance(grafo, Grafo) and isinstance(nodo, Nodo):
    if nodo not in grafo.nodos:
      grafo.nodos.add(nodo)
      return nodo
    raise ValueError('Nodo já existe neste grafo')
  raise TypeError('Grafo deve ser objeto do tipo grafo e o nó deve ser objeto do tipo Nodo')


def removerNodo(grafo, nodo):
  if isinstance(grafo, Grafo) and isinstance(nodo, Nodo):
    if nodo in grafo.nodos:
      grafo.nodos.remove(nodo)
      return nodo
    raise ValueError('Nó a ser removido não existe neste grafo')
  raise TypeError('Grafo deve ser objeto do tipo grafo e o nó deve ser objeto do tipo Nodo')
