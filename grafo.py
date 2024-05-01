class Graph:
  def __init__(self, vertex_count, edge_count, nodes):
    if isinstance(nodos, list) and isinstance(arestas, list) and isinstance(nmrNodos, int) and isinstance(nmrArestas, int):
      if nmrNodos >= 0 and nmrArestas >= 0:
        self.nmrNodos = nmrNodos
        self.nmrArestas = nmrArestas
      else:
        raise Exception('O valor que indica o número de nodos e o valor que indica o número de arestas deve ser maior ou igual a 0')
      if nmrNodos != len(nodos) or nmrArestas != len(arestas):
        raise Exception('O valor que indica o número de nodos e o que indica o número de arestas devem ser iguais, respectivamente, a quantidade de nodos e de arestas inseridos')
      self.nodos = {}
      for nodo in nodos:
        if isinstance(nodo, Nodo):
          self.nodes[nodo.id] = nodo
        else:
          raise Exception('Os nodos devem ser objetos do tipo Nodo')
    else:
      raise Exception('É preciso de um inteiro para representar o número de nodos, outro inteiro para o número de arestas, uma lista de nodos e uma lista de arestas')

  def is_neighbor(self, vertex_1, vertex_2):
    if isinstance(vertex_1, int) and isinstance(vertex_2, int):
      try:
        self.nodes[vertex_1]
      except KeyError:
        raise Except('O vértice passado não consta no grafo')
      try:
          return bool(vertex_1['edges'][vertex_2])
      except KeyError:
          return False
    raise Exception('Os vértices precisam ser passados como ID\'s do tipo int')

  def neighbors(self, vertex):
    if isinstance(vertex, int):
      try:
        vertex = self.nodes[vertex]
      except KeyError:
        raise Exception('O vértice não consta no grafo')
      return [key for key in vertex['edges'].keys()]
    raise Exception('O vértice precisa ser um ID do tipo int')

  def cost(self, vertex_1, vertex_2):
    if isinstance(vertex_1, int) and isinstance(vertex_2):
      try:
        vertex_1 = self.nodes[vertex_1]
        vertex_2 = self.nodes[vertex_2]
      except KeyError:
        raise Exception('Pelo menos um dos vértices não consta no grafo')
      neighbors = self.neighbors(vertex_1)
      try:
        index = neighbors.index(vertex_2)
      except ValueError:
        raise Exception('Os vértices não são vizinhos')
      return self.nodes[vertex_1]['edges'][vertex_2]
    else:
      raise Exception('Os vértices precisam ser passados como ID\'s do tipo int')


class Aresta:
  def __init__(self, nodo1, nodo2, custo):
    if isinstance(custo, float) and custo >= 0:
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


def read_graph(filename: str):
    """Lê uma estrutura de grafo de um arquivo e retorna a estrutura"""
    with open(filename, "rt") as input_file:
        vertex_count, nodes = int(input_file.readline().strip()), {}
        for _ in range(vertex_count):
            index, latitude, longitude = input_file.readline().strip().split()
            nodes[index] = {'lat': latitude, 'lon': longitude, 'edges': {}}
            
        edge_count = int(input_file.readline().strip())
        for _ in range(edge_count):
            from_vertex, to_vertex, cost = input_file.readline().strip().split()
            try:
              nodes[from_vertex]['edges'][to_vertex] = cost
              nodes[to_vertex]['edges'][from_vertex] = cost
            except KeyError:
              raise Exception('You are attempting to acess a node that doesn't exist')
        graph = Graph(vertex_count, edge_count, nodes)
    return graph
