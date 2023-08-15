def is_undirected(G):
    n = len(G)
    converted_G = convert(G)

    for v in range(n):
        for u in range(n):
            if (converted_G[v][u] and not converted_G[u][v]) or\
               (not converted_G[v][u] and converted_G[u][v]):
               return False
               
    return True


def convert(G):
    n = len(G)
    converted_G = [[0 for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for u in G[v]:
            converted_G[v][u] = 1
    
    return converted_G


if __name__ == "__main__":
    print(is_undirected([[2, 3], [2, 3], [0, 3, 1], [0, 2, 1, 4], [3]]))
    print(is_undirected([[3], [2, 3], [0, 3, 1], [0, 2, 1, 4], [3]]))
