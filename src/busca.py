from collections import deque
from queue import PriorityQueue

from funcoesGrafo import adjacente, vizinhos
from grafo import Grafo


def dfs (Grafo, start, goal):

  if not isinstance(Grafo, Grafo):
    raise Exception('O grafo deve ser do tipo Grafo')
  if start not in Grafo.nodos:
    raise Exception('O nodo de início deve ser um nodo registrado no grafo')
  if goal not in Grafo.nodos:
    raise Exception('O nodo a ser buscado deve ser um nodo registrado no grafo')

  visited = set()
  stack = [start]
  pre_path = {start: None}
  
  while stack:
    parent = v = stack.pop()

    if goal == v:
      visited.add(v)
      path = [v]
      actual = pre_path[pre_path[v]]
      custo = 0
      while actual is not None:
        path.append(actual)
        actual = pre_path[actual]
      for node in range(0, len(path), 2):
        edge = path[node].getEdge(path[node+1])
        custo += edge.custo
      return (len(visited), custo, path)

    if v not in visited:
      visited.add(v)
      for u in vizinhos(Grafo, v):
        if u not in visited:
          pre_path[u] = parent
        stack.append(u)


def bfs(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando busca em largura


def branch_and_bound(Grafo, start, goal):
  if start in Grafo.nodos and goal in Grafo.nodos:
    best_so_far = ()
    Q = deque()
    Q.appendleft(start)
    while Q:
      v = Q.pop()
      if goal == v:
        retur
    


def manhattan(a, b):
  return abs(a.lat - b.lat) + abs(a.lon - b.lon)

def a_star(graph, start, goal):
  frontier = PriorityQueue()
  frontier.put(0, start)
  came_from = {start: None}
  cost_so_far = {start: 0}

  while not frontier.empty():
    current = frontier.get()

    if current == goal:
      if came_from[current] is None:
        return [current]
      parent = came_from[current]
      path = [current, parent]
      while parent != start:
        parent = came_from[parent]
        path.append(parent)
      return (len(came_from.keys()), cost_so_far[current], reversed(path))

    for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + manhattan(goal, next)
         frontier.put(next, priority)
         came_from[next] = current


def dijkstra(Grafo, start, goal):
  dist, prev, Q = {}, {}, deque()
  for nodo in Grafo.nodos:
    dist[nodo] = float('inf')
    prev[nodo] = None
    Q.appendleft(nodo)
  dist[start] = 0

  while Q:
    #u = nodo com menor custo que existe em Q (no caso de uma iteração que está em start, u seria o próprio, pois ele tem custo 0, enquanto os outros tem custo infinito)
    Q.pop(u)

  # u == goal para baixo não existe no pseudocódigo do professor
  if u == goal:
    analisados = 0
    for key in prev.keys():
      if prev[key] != None
	    analisados += 1
    return (analisados, dist, [prev])

  for v in Graph.vizinhos(u):
    if v in Q:
      alt = dist[u] + Graph.arestas[u][v]
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
