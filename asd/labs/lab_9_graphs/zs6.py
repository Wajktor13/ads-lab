"""
2 krotne rozmnozenie miast
indeks oznacza kto wyjezdzal
nie moze byc krawedzi jace-jacek i marian-marian
tam gdzie jechal drugi dajemy 0
odpalamy 2xdijkstre chociaz chyba niekoniecznie ale 2 pkt startowe
"""


from heapq import *

ALICJA = 0
BOB = 1


def Dijkstra_double_edges_SWP(G, x, y, starting):
    n = len(G)
    visited = [[False, False] for _ in range(n)]
    distance = [[float('inf'), float('inf')] for _ in range(n)]
    parent = [[None, None] for _ in range(n)]
    Q = []
    current = (starting + 1) % 2

    heappush(Q, (0, x, current))
    visited[x][current], distance[x][current] = True, 0

    while len(Q) > 0:
        dst, v, driver = heappop(Q)
        visited[v][driver] = True
        
        if driver == ALICJA:
            for u, w in G[v]:
                if not visited[u][BOB] and distance[u][BOB] > distance[v][ALICJA]:
                    distance[u][BOB] = distance[v][ALICJA]
                    parent[u][BOB] = v
                    heappush(Q, (distance[u][BOB], u, BOB))
        
        else:
            for u, w in G[v]:
                if not visited[u][ALICJA] and distance[u][ALICJA] > distance[v][BOB] + w:
                    distance[u][ALICJA] = distance[v][BOB] + w
                    parent[u][ALICJA] = v
                    heappush(Q, (distance[u][ALICJA], u, ALICJA))

    return distance, parent


def min_path_for_Alicja(G, x, y):
    A_distance, A_parent = Dijkstra_double_edges_SWP(G, x, y, ALICJA)
    B_distance, B_parent = Dijkstra_double_edges_SWP(G, x, y, BOB)
    route = []

    if min(A_distance[y][ALICJA], A_distance[y][BOB]) < min(B_distance[y][ALICJA], B_distance[y][BOB]):
        if A_distance[y][ALICJA] < A_distance[y][BOB]:
            get_route(A_parent, y, ALICJA, route)
        else:
            get_route(A_parent, y, BOB, route)
        
        return 'Alicja', route

    else:
        if B_distance[y][ALICJA] < B_distance[y][BOB]:
            get_route(B_parent, y, ALICJA, route)
        else:
            get_route(B_parent, y, BOB, route)
        
        return 'Bob', route


def get_route(parent, last_v, ending_driver, route):
    driver = ending_driver
    v = last_v

    while v is not None:
        route.append(v)
        v = parent[v][driver]
        driver = (driver + 1) % 2
    
    route.reverse()
    route.append
            

if __name__ == "__main__":
    print(min_path_for_Alicja([[(1, 11), (3, 1), (4, 2)], [(0, 11), (2, 3), (4, 10)], [(4, 1), (1, 3)],
                               [(0, 1), (4, 8)], [(2, 1), (1, 10), (0, 2), (3, 8)]], 3, 1))
                               