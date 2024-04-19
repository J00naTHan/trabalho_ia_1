from grafo import Aresta, Grafo, Nodo

# retorna ValueError para tipo do arquivo

def ler_grafo(nome_arq):
  if not isinstance(nome_arq, str):
    raise ValueError(f'\nTipo recebido: {type(nome_arq)}, tipo esperado: str\n')

  if not nome_arq.endswith('.txt'):
    nome_arq += '.txt'

  # retorna FileNotFoundError para arquivo inexistente

  try:
    with open(nome_arq, 'r') as arq:
      nmr_nodos = nmr_arestas = cont = 0
      nodos, arestas, linhas = [], [], arq.readlines()

      for linha in linhas:
        palavras = linha.strip().split(' ')

        if len(palavras) == 1 and cont == 0:
          nmr_nodos = int(linha[0])
          cont += 1
        elif len(palavras) == 1 and cont == 1:
          nmr_arestas = int(linha[0])
          cont += 1

        elif len(palavras) == 3:

          if cont == 1:
            id = int(palavras[0])
            lat = float(palavras[1])
            lon = float(palavras[2])
            nodo = Nodo(id, lat, lon)
            nodos.append(nodo)

          elif cont == 2:
            id1, id2 = int(palavras[0]), int(palavras[1])
            if id1 in nodos and id2 in nodos:
              for nodo in range(len(nodos)):
                if nodos[nodo].id == id1:
                  nodo1 = nodos[nodo]
                elif nodos[nodo].id == id2:
                  nodo2 = nodos[nodo]
            custo = int(palavras[2])
            aresta = Aresta(nodo1, nodo2, custo)
            arestas.append(aresta)

    arq.close()
  except FileNotFoundError:
    raise FileNotFoundError(f'\nO arquivo "{nome_arq}" não foi encontrado\n')

  grafo = Grafo(nmr_nodos, nmr_arestas)
  grafo['nodos'] = nodos
  grafo['arestas'] = arestas
  return grafo
