from grafo import Aresta, Grafo, Nodo


# exception customizada para objetos procurados e que não foram encontrados em uma estrutura de dados
class ObjectNotFoundError(Exception):
  pass

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
        if linha.isspace():
          continue

        palavras = linha.strip().split(' ')

        if len(palavras) == 1 and cont == 0:
          try:
            nmr_nodos = int(linha[0])
          except ValueError:
            raise ValueError('\nO valor que deveria corresponder ao NÚMERO DE NODOS, encontrado no arquivo, não pode ser convertido para int (inteiro)\n')
          cont += 1

        elif len(palavras) == 1 and cont == 1:
          try:
            nmr_arestas = int(linha[0])
          except ValueError:
            raise ValueError('\nO valor que deveria corresponder ao NÚMERO DE ARESTAS, encontrado no arquivo, não pode ser convertido para int (inteiro)\n')
          cont += 1

        elif len(palavras) == 3:

          if cont == 1:
            try:
              id = int(palavras[0])
            except ValueError:
              raise ValueError('\nO valor que deveria corresponder ao ID de um nodo, encontrado no arquivo, não pode ser convertido para int (inteiro)\n')
            try:
              lat = float(palavras[1])
            except ValueError:
              raise ValueError('\nO valor que deveria corresponder a LATITUDE de um nodo, encontrado no arquivo, não pode ser convertido para float\n')
            try:
              lon = float(palavras[2])
            except ValueError:
              raise ValueError('\nO valor que deveria corresponder a LONGITUDE de um nodo, encontrado no arquivo, não pode ser convertido para float\n')
            nodo = Nodo(id, lat, lon)
            nodos.append(nodo)

          elif cont == 2:
            try:
              id1, id2 = int(palavras[0]), int(palavras[1])
            except ValueError:
              raise ValueError('\nO valor que deveria corresponder ao ID DE NO MÍNIMO UM DOS NODOS EXTREMOS DE UMA ARESTA, encontrado no arquivo, não pode ser convertido para int (inteiro)\n')
            if id1 in nodos and id2 in nodos:
              for nodo in range(len(nodos)):
                if nodos[nodo].id == id1:
                  nodo1 = nodos[nodo]
                elif nodos[nodo].id == id2:
                  nodo2 = nodos[nodo]
            else:
              raise ObjectNotFoundError('\nUm dos nós que deveria corresponder aos extremos de uma aresta não foi encontrado na lista de nodos\n')
            try:
              custo = int(palavras[2])
            except ValueError:
              raise ValueError('\nO valor que deveria corresponder ao CUSTO de uma aresta não pode ser convertido para int (inteiro)\n')
            aresta = Aresta(nodo1, nodo2, custo)
            arestas.append(aresta)

    arq.close()
  except FileNotFoundError:
    raise FileNotFoundError(f'\nO arquivo "{nome_arq}" não foi encontrado\n')

  grafo = Grafo(nmr_nodos, nmr_arestas)
  grafo['nodos'] = nodos
  grafo['arestas'] = arestas
  return grafo
