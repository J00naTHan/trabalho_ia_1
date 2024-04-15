class Grafo:
  def __init__(self, nmrNodos = 0, nmrArestas = 0):
    self.nmrNodos = nmrNodos if isinstance(nmrNodos, int) and nmrNodos >= 0 else 0
    self.nmrArestas = nmrArestas if isinstance(nmrArestas, int) and nmrArestas >= 0 else 0
    self.nodos = set()
    self.arestas = set()

  def __getitem__(self, chave):
    if chave == 'nodos':
      return self.nodos
    elif chave == 'arestas':
      return self.arestas
    raise KeyError(f'A chave "{chave}" não existe')

  def __setitem__(self, chave, valor):
    if isinstance(valor, set):
      if chave == 'nodos':
        self.nodos = valor
      elif chave == 'arestas':
        self.arestas = valor
      raise KeyError(f'A chave "{chave}" não existe')
    raise TypeError(f'O valor para a chave "{chave}" deve ser do tipo set')


class Aresta:
  def __init__(self, nodo1, nodo2, custo):
    if isinstance(custo, int) and custo >= -1:
      self.custo = custo
    else:
      raise TypeError('O custo para essa aresta deve ser do tipo int (inteiro) e deve ser maior ou igual a -1')
    if isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
      self.nodo1 = nodo1
      self.nodo2 = nodo2
    else:
      raise TypeError('Nodos devem ser objetos do tipo Nodo')


class Nodo:
  def __init__(self, id, longitude, latitude):
    if isinstance(id, int) and isinstance(longitude, int) and isinstance(latitude, int):
      self.id = id
      # não sei se latitude e longitude possuem um limite de valor e se são inteiros
      self.lat = latitude
      self.lon = longitude
      self.arestas = set()
    else:
      raise TypeError('Um nodo requer 1 valor do tipo inteiro para id, e 2 valores do tipo float para latitude e longitude')

  def __eq__(self, nodo):
    if isinstance(nodo, Nodo):
      return self.id == nodo.id
    raise TypeError('A comparação deve ser feita com outro objeto do tipo Nodo')
