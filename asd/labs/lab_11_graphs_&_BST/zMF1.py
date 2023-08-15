from collections import deque


def max_flow(G, s, t):
    n = len(G)
    F = [[0 for _ in range(n)] for _ in range(n)]
    RG = [[G[u][v] for v in range(n)] for u in range(n)]
    
    enl_path, min_flow = BFS(RG, s, t)
    while enl_path is not None:
        update_max_flow(F, enl_path, min_flow, t)
        update_residual_graph(RG, G, F, enl_path, t)
        enl_path, min_flow = BFS(RG, s, t)
    
    return F


def update_max_flow(F, parent, min_flow, t):
    v = parent[t]
    F[v][t] += min_flow
    while parent[v] is not None:
        F[parent[v]][v] += min_flow
        v = parent[v]


def update_residual_graph(RG, G, F, parent, t):
    v = parent[t]
    RG[v][t] = G[v][t] - F[v][t]
    RG[t][v] = G[t][v] + F[v][t]
    RG[t][v] = F[v][t]
    while parent[v] is not None:
        RG[parent[v]][v] = G[parent[v]][v] - F[parent[v]][v]
        RG[v][parent[v]] = G[v][parent[v]] + F[v][parent[v]]
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
    flow = max_flow([[0, 5, 0, 1, 0, 0],
                     [5, 0, 4, 0, 1, 0],
                     [0, 4, 0, 1, 0, 3],
                     [1, 0, 1, 0, 1, 0],
                     [0, 1, 0, 1, 0, 10],
                     [0, 0, 3, 0, 10, 0]], 0, 5)
    
    for row in flow:
        print(row)
