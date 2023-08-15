def Floyd_Warshall(G): # G = [[(u, w)]]
    n = len(G)
    parent = [[None for _ in range(n)] for _ in range(n)]
    D = create_distance_matrix(G)

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if D[u][k] + D[k][v] < D[u][v]:
                    D[u][v] = D[u][k] + D[k][v]
                    parent[u][v] = k

    return D, parent


def create_distance_matrix(G):
    n = len(G)
    D = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]

    for u in range(n):
        for v, w in G[u]:
            D[u][v] = w
    
    return D
