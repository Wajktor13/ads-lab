def passerby_closing(G):
    n = len(G)
    distance = [[G[u][v] if G[u][v] >= 0 else float('inf') for v in range(n)] for u in range(n)]

    for k in range(n):
        for v in range(n):
            for u in range(n):
                distance[v][u] = min(distance[v][u], distance[v][k] + distance[k][u])
    
    return distance
