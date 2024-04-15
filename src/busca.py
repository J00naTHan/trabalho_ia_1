from queue import PriorityQueue


def dfs(graph, start, goal):
	# busca em graph, um caminho entre start e goal usando busca em profundidade
	assert (start in graph.nodo)
	assert (goal in graph.nodo)


def bfs(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando busca em largura

def branch_and_bound(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando Branch and Bound

def a_star(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando A*

def dijkstra(graph, start: int, goal: int) -> (int, int, [int]):
	# busca em graph, um caminho entre start e goal usando Dijkstra
