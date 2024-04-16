from grafo import Aresta, Grafo, Nodo


def ler_grafo(nomeArq):
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
        if cont == 1:
          id = int(linha[0])
          lat = float(linha[1])
          lon = float(linha[2])
          nodo = Nodo(id, lat, lon)
          nodos.append(nodo)
        elif cont == 2:
          id1, id2 = int(linha[0]), int(linha[1])
          if id1 in nodos and id2 in nodos:
            for nodo in range(0, len(nodos) - 1):
              if nodos[nodo].id == id1:
                nodo1 = nodos[nodo]
              elif nodos[nodo].id == id2:
                nodo2 = nodos[nodo]
          custo = int(linha[2])
          aresta = Aresta(nodo1, nodo2, custo)
          arestas.append(aresta)
  arq.close()

  grafo = Grafo(nmrNodos, nmrArestas)
  grafo['nodos'] = nodos
  grafo['arestas'] = arestas
  return grafo
