def dfs(graph, start, goal):
	"""Busca em graph, um caminho entre start e goal usando busca em profundidade."""
	anNodes = int('1')
	pathLen = int('1')
	startToGoal = int('1')
	return tuple(anNodes, pathLen, startToGoal)

def bfs(graph, start: int, goal: int) -> (int, int, [int]):
	"""Busca em graph, um caminho entre start e goal usando busca em largura."""

def branch_and_bound(graph, start: int, goal: int) -> (int, int, [int]):
	"""Busca em graph, um caminho entre start e goal usando Branch and Bound."""

def a_star(graph, start: int, goal: int) -> (int, int, [int]):
	"""Busca em graph, um caminho entre start e goal usando A*."""

def dijkstra(graph, start: int, goal: int) -> (int, int, [int]):
	"""Busca em graph, um caminho entre start e goal usando Dijkstra."""
