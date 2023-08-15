"""
Wiktor Wilkusz 411605
Program konwertuje E oraz S na graf postaci G = [[(u,w), ...], ...],
przy czym każde 2 wierzchołki z S zostają dodane do G z wagą 0.
Następnie wykonywany jest algorytm Dijkstry.

Złożoność: O(n^2)
"""


from kol3atesty import runtests


def convert_graph(n, E, S):
    G = [[-1 for _ in range(n)] for _ in range(n)]

    for u, v, t in E:
        G[u][v] = G[v][u] = t

    for i in range(len(S) - 1):
        p1 = S[i]
        for j in range(i + 1, len(S)):
            p2 = S[j]
            G[p1][p2] = G[p2][p1] = 0

    return G


def spacetravel( n, E, S, a, b ):
    G = convert_graph(n, E, S)
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[a] = 0

    for _ in range(n):
        u = get_min_v(visited, distance)
        visited[u] = True

        for v in range(n):
            if G[u][v] >= 0 and not visited[v]:
                relax(distance, u, v, G[u][v])

    return distance[b] if distance[b] != float('inf') else None


def relax(distance, u, v, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w


def get_min_v(visited, distance):
    n = len(visited)
    min_v = None

    for v in range(n):
        if not visited[v] and (min_v is None or distance[v] < distance[min_v]):
            min_v = v
    
    return min_v

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
