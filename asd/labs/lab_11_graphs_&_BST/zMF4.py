from collections import deque


def maximum_bipartite_matching(G): # G := [[u, ..], ...]
    mbm = []
    converted_G = convert(G)
    n = len(converted_G)

    max_flow(converted_G, n - 2, n - 1, mbm)
    
    return mbm


def convert(G):
    n = len(G)
    converted_G = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    set_0, set_1 = separate_vertices(G) 

    for u in set_0:
        for v in G[u]:
            converted_G[u][v] = 1

        converted_G[n][u] = 1
    
    for u in set_1:
        converted_G[u][n + 1] = 1
    
    return converted_G


def separate_vertices(G):
    Q = deque()
    n = len(G)
    colour = [-1 for _ in range(n)]

    for s in range(n):
        if colour[s] >= 0:
            continue

        Q.append(s)
        colour[s] = 0

        while Q:
            u = Q.pop()
            for v in G[u]:
                if colour[v] < 0:
                    colour[v] = (colour[u] + 1) % 2
                    Q.append(v)
    
    set_0, set_1 = [], []

    for v in range(n):
        if colour[v] == 0:
            set_0.append(v)
        else:
            set_1.append(v)
    
    return set_0, set_1


def max_flow(G, s, t, mbm):
    n = len(G)
    F = [[0 for _ in range(n)] for _ in range(n)]
    RG = [[G[u][v] for v in range(n)] for u in range(n)]
    
    enl_path, min_flow = BFS(RG, s, t)
    while enl_path is not None:
        update_max_flow_and_mbm(F, enl_path, min_flow, t, mbm)
        update_residual_graph(RG, G, F, enl_path, t)
        enl_path, min_flow = BFS(RG, s, t)
    

def update_max_flow_and_mbm(F, parent, min_flow, t, mbm):
    n = len(F)
    v = parent[t]
    F[v][t] += min_flow

    if v not in (n - 1, n - 2) and t not in (n - 1, n - 2):
        mbm.append((v, t))
        
    while parent[v] is not None:
        if parent[v] not in (n - 1, n - 2) and v not in (n - 1, n - 2):
            mbm.append((parent[v], v))

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


if __name__ == "__main__":
    print(maximum_bipartite_matching([[1, 2], [0, 3, 4, 5], [6, 7, 0], [1], [1], [1], [2, 8, 9, 10], [2], [6], [6], [6]]))
