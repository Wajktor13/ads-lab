"""Wiktor Wilkusz 411605
Algorytm znajduje odległości wierzchołków od s za pomocą BFS, a następnie
sprawdza, jaka jest minimalna odległość od s każdego wierzchołka sąsiadującego
z t oraz ile wierzchołków posiadą tą odległość. Jeśli istnieje jeden - to da się
wydłużyć scieżkę. Jeśli nie, to sprawdzamy, czy na ścieżce jest most.
"""


from zad6testy import runtests
from collections import deque


def longer( G, s, t ):
    n = len(G)
    parent, distance = BFS_get_distance(G, s)

    if distance[t] is None:
        return None
    
    min_dstc = float('inf')
    min_dstc_count = None
    best_v = None

    for n in G[t]:
        d = distance[n]
        if d is not None:
            if d < min_dstc:
                min_dstc = d
                min_dstc_count = 1
                best_v = n
            elif d == min_dstc:
                min_dstc_count += 1
    
    if min_dstc_count >= 2:
        bridges = DFS_bridges(G)
        route = []
        v = t
        while v is not None and parent[v] is not None:
            route.append([v, parent[v]])
            v = parent[v]

        for b in bridges:
            for e in route:
                if b == e or b == list(reversed(e)):
                    return e
                    
    else:
        return (best_v, t)


def BFS_get_distance(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [None for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()

    visited[s] = True
    distance[s] = 0
    Q.append(s)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                parent[u] = v
                Q.append(u)
    
    return parent, distance


def DFS_bridges(G):
    def DFS_visit(v):
        nonlocal current_time

        visited[v] = True
        time[v] = low[v]  = current_time
        current_time += 1

        for s in G[v]:
            if visited[s] and v not in child[s]:
                low[v] = min(low[v], low[s])
            elif not visited[s]:
                parent[s] = v
                child[v].append(s)
                DFS_visit(s)

        for c in child[v]:
            low[v] = min(low[v], low[c])

        if low[v] == time[v] and parent[v] is not None:
            bridges.append([parent[v], v])

    n = len(G)
    visited = [False for _ in range(n)]
    time = [None for _ in range(n)]
    low = [None for _ in range(n)]
    child = [[] for _ in range(n)]
    parent = [None for _ in range(n)]
    bridges = []
    current_time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)

    return bridges
    
            
runtests( longer, all_tests = True )
