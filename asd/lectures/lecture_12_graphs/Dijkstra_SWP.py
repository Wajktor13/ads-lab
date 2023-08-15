from queue import PriorityQueue


def Dijkstra(G):
    n = len(G)
    PQ = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[0] = 0
    PQ.put((0, 0))

    while not PQ.empty():
        v = PQ.get()[1]
        if visited[v]:
            continue
        
        visited[v] = True

        for s, w in G[v]:
            if not visited[s]:
                relax(v, s, w, parent, distance)
                PQ.put((distance[s], s))
    
    return parent, distance


def relax(v, s, w, parent, distance):
    if distance[s] > distance[v] + w:
        distance[s] = distance[v] + w
        parent[s] = v


##############################################
def Dijkstra_matrix(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[0] = 0

    for _ in range(n):
        v = get_min_v(visited, distance)
        visited[v] = True

        for u in range(n):
            if G[v][u] >= 0 and not visited[u]:
                relax(v, u, G[v][u], parent, distance)

    return parent, distance


def get_min_v(visited, distance):
    n = len(visited)
    min_v = None

    for v in range(n):
        if not visited[v] and (min_v is None or distance[v] < distance[min_v]):
            min_v = v
    
    return min_v
