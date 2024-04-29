from collections import deque
from queue import PriorityQueue

from funcoesGrafo import adjacente, vizinhos
from grafo import Grafo


def dfs (Grafo, start, goal):

  if not isinstance(Grafo, Grafo):
    raise Exception('O grafo deve ser do tipo Grafo')
  elif start not in Grafo.nodos:
    raise Exception('O nodo de início deve ser um nodo registrado no grafo')
  elif goal not in Grafo.nodos:
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


def branch_and_bound(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando Branch and Bound


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


def dijkstra(Graph, start, goal):
  return (int, int, [int])
