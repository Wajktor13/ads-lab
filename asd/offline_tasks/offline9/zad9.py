from zad9testy import runtests
from collections import deque

def maxflow(G, s):
    n = vertices_amount(G)
    result = -1

    for u in range(n - 1):
        if u == s:
            continue
        for v in range(u + 1, n):
            if v == s:
                continue

            result = max(result, count_max_flow(convert(G, u, v), s, n))
    
    return result


def count_max_flow(G, s, t):
    n = len(G)
    F = [[0 for _ in range(n)] for _ in range(n)]
    RG = [[G[u][v] for v in range(n)] for u in range(n)]
    
    enl_path, min_flow = BFS(RG, s, t)
    while enl_path is not None:
        update_max_flow(F, enl_path, min_flow, t)
        update_residual_graph(RG, G, F, enl_path, t)
        enl_path, min_flow = BFS(RG, s, t)
    
    flow = 0
    for v in range(n):
        flow += F[v][n - 1]

    return flow


def update_max_flow(F, parent, min_flow, t):
    v = parent[t]
    F[v][t] += min_flow
    while parent[v] is not None:
        F[parent[v]][v] += min_flow
        v = parent[v]


def update_residual_graph(RG, G, F, parent, t):
    v = parent[t]
    RG[v][t] = G[v][t] - F[v][t]
    RG[t][v] = F[v][t]
    while parent[v] is not None:
        RG[parent[v]][v] = G[parent[v]][v] - F[parent[v]][v]
        RG[v][parent[v]] = F[parent[v]][v]
        v = parent[v]
    

def BFS(G, s, t):
    Q = deque()
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    min_flow = [float('inf') for _ in range(n)]

    Q.append(s)
    visited[s] = True

    while Q:
        u = Q.pop()
        for v in range(n):
            if G[u][v] > 0 and not visited[v]:
                min_flow[v] = min(G[u][v], min_flow[u])
                visited[v], parent[v] = True, u
                Q.append(v)
        
        if visited[t]:
            return parent, min_flow[t]

    return None, None


def convert(G, v1, v2):
    n = vertices_amount(G)
    converted_G = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for u, v, w in G:
        converted_G[u][v] = w
    
    converted_G[v1][n] = converted_G[v2][n] = float('inf')

    return converted_G


def vertices_amount(G):
    n = 0
    for u, v, w in G:
        n = max(n, u, v)
    n += 1

    return n

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
