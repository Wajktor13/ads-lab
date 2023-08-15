"""czytac dajkstra"""

from queue import PriorityQueue

def Dijkstra(G): #G:=[[(w, v)]]
    n = len(G)
    PQ = PriorityQueue()
    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[0] = 0
    PQ.put((0, 0))


    while not PQ.empty():
        e = (PQ.get())[1]
        if visited[e]:
            continue

        visited[e] = True
        for u, d in G[e]:
            if not visited[u] and distance[e] + d < distance[u]:
                distance[u] = distance[e] + d
                PQ.put(distance[u], u)
    
    return distance
              