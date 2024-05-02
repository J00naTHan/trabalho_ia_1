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


def bfs(graph, start, goal):
    if not start in graph.nodes or not goal in graph.nodes:
        raise Exception('Os nodos de largada e chegada não existem no grafo')
    Q, visited = deque(), set()
    Q.appendleft(start)
    while Q:
        v = Q.pop()
	if goal == v:
	    return ()
	if v not in visited:
	    visited.add(v)
	    for u in graph.neighbors(v):
                Q.appendleft(u)


def branch_and_bound(graph, start, goal):
    if start not in graph.nodes and goal not in graph.nodes:
        raise Exception('Os nodos de largada e chegada não existem no grafo')
    best_so_far, Q = (None, float('inf')), deque()
    Q = deque()
    Q.appendleft(start)

    while Q:
        v = Q.pop()

        if goal == v:
            return ()
    


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


def dijkstra(graph, start, goal):
  dist, prev, Q = {}, {}, deque() #não sei se Q é deque ou priorityqueue, nem se a priorityqueue normal pode ser usada ou tem q ser uma criada
  for node in graph.nodes:
    dist[node], prev[node] = float('inf'), None
    Q.appendleft(nodo)
  dist[start] = 0

  while Q:
    u = min(Q)
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
