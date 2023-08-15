from queue import PriorityQueue


def Prim_MST(G): # G:=[[(v, weight)]]
    n = len(G)
    PQ = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    priority = [float('inf') for _ in range(n)]
    priority[0] = 0
    PQ.put((0, 0))

    while not PQ.empty():
        v = PQ.get()[1]        
        visited[v] = True

        for s, w in G[v]:
            if not visited[s] and priority[s] > w:
                priority[s] = w
                parent[s] = v            
                PQ.put((priority[s], s))
    
    return parent


##################################################
def Prim_MST_matrix(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    priority = [float('inf') for _ in range(n)]

    priority[0] = 0
    
    for _ in range(n):
        v = get_min_v(visited, priority)
        visited[v] = True

        for u in range(n):
            if G[v][u] >= 0 and not visited[u] and priority[u] > G[v][u]:
                priority[u] = G[v][u]
                parent[u] = v
    
    return parent


def get_min_v(visited, priority):
    n = len(visited)
    min_v = None

    for v in range(n):
        if not visited[v] and (min_v is None or priority[v] < priority[min_v]):
            min_v = v
    
    return min_v


if __name__ == "__main__":
    print(Prim_MST([[(1, 11), (3, 1), (4, 2)], [(0, 11), (2, 3), (4, 10)], [(4, 1), (1, 3)],
                    [(0, 1), (4, 8)], [(2, 1), (1, 10), (0, 2), (3, 8)]]))
    
    print(Prim_MST_matrix([[-1, 11, -1, 1, 2],
                           [11, -1, 3, -1, 10],
                           [-1, 3, -1, -1, 1],
                           [1, -1, -1, -1, 8],
                           [2, 10, 1, 8, -1],]))
                           