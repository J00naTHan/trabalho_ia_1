from grafo import Grafo
from nodos import Aresta, Nodo


def lerGrafo(nomeArq):
  if not isinstance(nomeArq, str):
    raise TypeError(f"'Erro: tipo recebido: {type(nomeArq)}, tipo esperado: str'")

  if not nomeArq.endswith('.txt'):
    nomeArq += '.txt'

  with open(nomeArq) as arq:
    nmrNodos = nmrArestas = cont = 0
    nodos = []
    arestas = []
    linhas = arq.readlines()

    for linha in linhas:
      linha = linha.strip().split(' ')

      if len(linha) == 1 and cont == 0:
        nmrNodos = int(linha[0])
        cont += 1
      elif len(linha) == 1 and cont == 1:
        nmrArestas = int(linha[0])
        cont += 1
      elif len(linha) == 3:
        temp = []
        for item in linha:
          item = int(item)
          temp.append(item)
        if cont == 1:
          nodo = Nodo(temp[0], temp[1], temp[2])
          nodos.append(nodo)
        elif cont == 2:
          aresta = Aresta(temp[0], temp[1], temp[2])
          arestas.append(aresta)
  arq.close()

  grafo = Grafo(nmrNodos, nmrArestas)
  grafo[nodos] = nodos
  grafo[arestas] = arestas
  return grafo
