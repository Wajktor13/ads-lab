from queue import PriorityQueue


def Dijkstra(G, x, y):
    n = len(G)
    PQ = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[x] = 0
    PQ.put((0, x, float('inf')))

    while not PQ.empty():
        d, v, prev_e = PQ.get()
        if visited[v]:
            continue
        
        visited[v] = True

        for s, w in G[v]:
            if not visited[s] and w < prev_e:
                relax(v, s, w, parent, distance)
                PQ.put((distance[s], s, w))
        
        if visited[y]:
            break
    
    route = []
    get_route(parent, route, y)

    return route[::-1], distance[y]


def relax(v, s, w, parent, distance):
    if distance[s] > distance[v] + w:
        distance[s] = distance[v] + w
        parent[s] = v


def get_route(parent, route, v):
    route.append(v)
    if parent[v] is not None:
        get_route(parent, route, parent[v])


if __name__ == "__main__":
    print(Dijkstra([[(2, 1), (3, 9), (1, 10)], [(4, 2)], [(3, 4)], [(5, 5)], [(3, 11), (5, 1)], []], 0, 5))
    