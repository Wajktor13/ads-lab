from math import log2


def currencies(K):
    n = len(K)
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    convert_wiegths_to_log2(K)
    distance[0] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                w = K[u][v]
                relax(u, v, w, parent, distance)
    
    for u in range(n):
        for v in range(n):
            w = K[u][v]
            if distance[v] > distance[u] + w:
                return True, u
    
    return False, None


def relax(u, v, w, parent, distance):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        parent[v] = u


def convert_wiegths_to_log2(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            G[u][v] = log2(G[u][v])


if __name__ == "__main__":
    print(currencies([[7, 15, 2, 2, 4],
                      [4, 3, 0.8, 5, 49],
                      [6, 5, 2, 0.9, 9],
                      [500, 0.7, 61, 9, 11],
                      [31, 10, 21, 11, 12],]))
