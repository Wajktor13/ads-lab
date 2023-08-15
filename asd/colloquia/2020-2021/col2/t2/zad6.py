"""Wiktor Wilkusz 411605
Algorytm znajduje odległości wierzchołków od s za pomocą BFS, a następnie
sprawdza, jaka jest minimalna odległość od s każdego wierzchołka sąsiadującego
z t oraz ile wierzchołków posiadą tą odległość. Jeśli istnieje jeden - to da się
wydłużyć scieżkę.
"""


from zad6testy import runtests
from collections import deque


def longer( G, s, t ):
    V = len(G)
    distance = [None for _ in range(V)]
    BFS_get_distance(G, distance, s)

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
        return None
    else:
        return (best_v, t)


def BFS_get_distance(G, distance, s):
    V = len(G)
    visited = [False for _ in range(V)]
    Q = deque()

    visited[s] = True
    distance[s] = 0
    Q.append(s)

    while Q:
        u = Q.popleft()
        for n in G[u]:
            if not visited[n]:
                visited[n] = True
                distance[n] = distance[u] + 1
                Q.append(n)
    
            
runtests( longer, all_tests = True )
