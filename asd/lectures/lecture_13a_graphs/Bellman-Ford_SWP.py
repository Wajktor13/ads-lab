def Bellman_Ford(G): # G:=[[(v, weight)]]
    n = len(G)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    distance[0] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                relax(u, v, w, parent, distance)
    
    for u in range(n):
        for v, w in G[u]:
            if distance[v] > distance[u] + w:
                return None
    
    return distance, parent


def relax(u, v, w, parent, distance):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u
