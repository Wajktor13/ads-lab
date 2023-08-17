from collections import deque


def BFS(G, v):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [None for _ in range(n)]
    parent = [None for _ in range(n)]

    Q = deque()

    visited[v], distance[v] = True, 0
    Q.append(v)

    while Q:
        v = Q.popleft()
        for s in G[v]:
            if not visited[s]:
                visited[s], distance[s], parent[s] = True, distance[v] + 1, v
                Q.append(s)
