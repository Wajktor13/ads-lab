"""
czy zawiera dobry pocz
1robimy na odwrot

2z kazdego v
usuwamy krawedzie

utrudnienie: ile dobrych - tak jak w 2 tylko nie usuwamy

"""

def good_begginings(G):
    n = len(G)
    distance = [[G[u][v] if G[u][v] >= 0 else float('inf') for v in range(n)] for u in range(n)]

    for k in range(n):
        for v in range(n):
            for u in range(n):
                distance[v][u] = min(distance[v][u], distance[v][k] + distance[k][u])
    
    save = []
    for v in range(n):
        for u in range(n):
            if v == u:
                continue
            elif distance[v][u] == float('inf'):
                break
        else:
            save.append(v)

    return save


if __name__ == "__main__":
    print(good_begginings([[-1, 1, -1, 1, -1, -1, 1],
                           [1, -1, 1, -1, -1, -1, -1],
                           [-1, -1, -1, 1, -1, -1, -1],
                           [-1, -1, -1, -1, 1, 1, -1],
                           [-1, -1, -1, -1, -1, -1, -1],
                           [-1, -1, -1, -1, -1, -1, -1],
                           [1, -1, -1, -1, -1, -1, -1]]))
