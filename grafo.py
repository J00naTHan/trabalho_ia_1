class Graph:
  def __init__(self, vertex_count, edge_count, nodes):
    if isinstance(nodes, dict) and isinstance(vertex_count, int) and isinstance(edge_count, int):
      if vertex_count >= 0 and edge_count >= 0:
        self.vertex_count = vertex_count
        self.edge_count = edge_count
      else:
        raise Exception('O valor que indica o número de nodos e o valor que indica o número de arestas deve ser maior ou igual a 0')
      if vertex_count != len(nodes.keys()):
        raise Exception('O valor que indica o número de nodos deve ser igual a quantidade de nodos inseridos')
      self.nodes = nodes
    else:
      raise Exception('É preciso de um inteiro para representar o número de nodos, outro inteiro para o número de arestas, uma lista de nodos e uma lista de arestas')

  def is_neighbor(self, vertex_1, vertex_2):
    if isinstance(vertex_1, int) and isinstance(vertex_2, int):
      try:
        self.nodes[vertex_1]
      except KeyError:
        raise Exception('O vértice passado não consta no grafo')
      try:
          return bool(self.nodes[vertex_1]['edges'][vertex_2])
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
    if isinstance(vertex_1, int) and isinstance(vertex_2, int):
      try:
        vertex_1 = self.nodes[vertex_1]
        vertex_2 = self.nodes[vertex_2]
      except KeyError:
        raise Exception('Pelo menos um dos vértices não consta no grafo')
      neighbors = self.neighbors(vertex_1)
      try:
        neighbors.index(vertex_2)
      except ValueError:
        raise Exception('Os vértices não são vizinhos')
      return self.nodes[vertex_1]['edges'][vertex_2]
    else:
      raise Exception('Os vértices precisam ser passados como ID\'s do tipo int')


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
          raise Exception('You are attempting to acess a node that doesn\'t exist')
    graph = Graph(vertex_count, edge_count, nodes)
  return graph
