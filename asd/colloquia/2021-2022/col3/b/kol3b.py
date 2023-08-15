from kol3btesty import runtests


def convert_graph(G, A):
    n = len(G)
    converted_G = [[-1 for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for u, w in G[v]:
            converted_G[v][u] = w

    for u in range(n - 1):
        for v in range(1, u):
            if converted_G[u][v] < 0:
                converted_G[u][v] = converted_G[v][u] = A[u] + A[v]
            else:
                converted_G[u][v] = min(converted_G[u][v], A[u] + A[v])

    return converted_G


def airports(G, A, s, t):
    converted_G = convert_graph(G, A)
    n = len(converted_G)
    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    distance[s] = 0

    for _ in range(n):
        u = get_min_v(visited, distance)
        visited[u] = True

        for v in range(n):
            if converted_G[u][v] >= 0 and not visited[v]:
                relax(distance, u, v, converted_G[u][v])

    return distance[t] if distance[t] != float('inf') else None


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
runtests( airports, all_tests = True )
