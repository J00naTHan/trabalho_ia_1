class Grafo:
  def __init__(self, nmrNodos, nmrArestas, nodos):
    if isinstance(nodos, list) and isinstance(nmrNodos, int) and isinstance(nmrArestas, int):
      if nmrNodos >= 0 and nmrArestas >= 0:
        self.nmrNodos = nmrNodos
        self.nodos = {}
      else:
        raise Exception('O valor que indica o número de nodos e o valor que indica o número de arestas deve ser maior ou igual a 0')
      if nmrNodos != len(nodos):
        raise Exception('O valor que indica o número de nodos deve ser igual a quantidade de nodos inseridos')

      for nodo in nodos:
        if isinstance(nodo, Nodo):
          self.nodos[nodo.id] = {nodo}
        else:
          raise Exception('Os nodos devem ser objetos do tipo Nodo')
    else:
      raise Exception('É preciso de um inteiro para representar o número de nodos, outro inteiro para o número de arestas e uma lista de nodos')


class Aresta:
  def __init__(self, nodo1, nodo2, custo):
    if isinstance(custo, int) and custo >= -1:
      self.custo = custo
    else:
      raise Exception('O custo para essa aresta deve ser do tipo int (inteiro) e deve ser maior ou igual a -1')
    if isinstance(nodo1, Nodo) and isinstance(nodo2, Nodo):
      self.nodo1 = nodo1
      self.nodo2 = nodo2
    else:
      raise Exception('Nodos devem ser objetos do tipo Nodo')


class Nodo:
  def __init__(self, id, latitude, longitude):
    if isinstance(id, int) and isinstance(longitude, float) and isinstance(latitude, float):
      self.id = id
      self.lat = latitude
      self.lon = longitude
      self.arestas = {}
    else:
      raise Exception('Um nodo requer 1 valor do tipo int (inteiro) para id, e 2 valores do tipo float para latitude e longitude')

  def __eq__(self, nodo):
    if isinstance(nodo, Nodo):
      return self.id == nodo.id
    elif isinstance(nodo, int):
      return self.id == nodo
    raise ValueError('A comparação deve ser feita com outro objeto do tipo Nodo ou do tipo int (inteiro)')

  def __hash__(self):
    return hash(self.id)
