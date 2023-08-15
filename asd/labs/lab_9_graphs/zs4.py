from math import log2
from queue import PriorityQueue


def shortest_path(G, s, e):
    n = len(G)
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    distance[s] = 1

    for _ in range(n - 1):
        for v in range(n):
            for u, w in G[v]:
                if distance[u] > distance[v] * w:
                    distance[u] = distance[v] * w
                    parent[u] = v
    
    for v in range(n):
        for u, w in G[v]:
            if distance[u] > distance[v] * w:
                return None

    route = []
    get_route(parent, route, e)

    return distance[e], route[::-1]


def get_route(parent, route, v):
    route.append(v)
    if parent[v] is not None:
        get_route(parent, route, parent[v])


#######################################################
def shortest_path_logarithms(G, s, e):
    n = len(G)
    PQ = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    convert_wiegths_to_log2(G)
    distance[s] = 0
    PQ.put((0, s))

    while not PQ.empty():
        v = PQ.get()[1]
        if visited[v]:
            continue
        
        visited[v] = True

        for s, w in G[v]:
            if not visited[s] and distance[s] > distance[v] + w:
                distance[s] = distance[v] + w
                parent[s] = v
                PQ.put((distance[s], s))
    
        if visited[e]:
            break

    route = []
    get_route(parent, route, e)


    return 2 ** distance[e], route[::-1]


def convert_wiegths_to_log2(G):
    for u in range(len(G)):
        for i in range(len(G[u])):
            v, w = G[u][i]
            G[u][i] = (v, log2(w))


if __name__ == "__main__":
    print(shortest_path([[(1, 11), (4, 2)], [(2, 3)], [], [(0, 1), (4, 8)], [(1, 10), (2, 1)]], 3, 1))
    print(shortest_path_logarithms([[(1, 11), (4, 2)], [(2, 3)], [], [(0, 1), (4, 8)], [(1, 10), (2, 1)]], 3, 1))
    