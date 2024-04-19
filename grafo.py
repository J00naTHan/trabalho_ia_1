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
    if chave == 'nodos':
      if isinstance(valor, set):
        self.nodos = valor
      elif isinstance(valor, list):
        self.nodos = set(valor)
      else:
        raise ValueError(f'O valor para a chave "{chave}" deve ser do tipo set ou lista')
    elif chave == 'arestas':
      if isinstance(valor, set):
        self.arestas = valor
      elif isinstance(valor, list):
        self.arestas = set(valor)
      else:
        raise ValueError(f'O valor para a chave "{chave}" deve ser do tipo set ou lista')
    else:
      raise KeyError(f'A chave "{chave}" não existe')


class Aresta:
  def __init__(self, nodo1, nodo2, custo):
    if isinstance(custo, int) and custo >= -1:
      self.custo = custo
    else:
      raise ValueError('O custo para essa aresta deve ser do tipo int (inteiro) e deve ser maior ou igual a -1')
    if isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
      self.nodo1 = nodo1
      self.nodo2 = nodo2
    else:
      raise ValueError('Nodos devem ser objetos do tipo Nodo')


class Nodo:
  def __init__(self, id, latitude, longitude):
    if (isinstance(id, int) and (isinstance(longitude, float) and longitude < 0) and (isinstance(latitude, float) and latitude < 0)):
      self.id = id
      self.lat = latitude
      self.lon = longitude
      self.arestas = set()
    else:
      raise ValueError('Um nodo requer 1 valor do tipo int (inteiro) para id, e 2 valores do tipo float para latitude e longitude')

  def __eq__(self, nodo):
    if isinstance(nodo, Nodo):
      return self.id == nodo.id
    elif isinstance(nodo, int):
      return self.id == nodo
    raise ValueError('A comparação deve ser feita com outro objeto do tipo Nodo ou do tipo int (inteiro)')

  def __hash__(self):
    return hash(self.id)
