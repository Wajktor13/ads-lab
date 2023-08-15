from copy import deepcopy


def best_root(G): # G = [[(u, w)]]
    n = len(G)
    D = deepcopy(G)

    for u in range(n):
        for v in range(n):
            if D[u][v] < 0:
                D[u][v] = float('inf')

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if D[u][k] + D[k][v] < D[u][v]:
                    D[u][v] = D[u][k] + D[k][v]

    br , max_dst = None, float('inf')
    for v in range(n):
        curr_max_dst = -float('inf')
        for u in range(n):
            if D[u][v] < float('inf') and curr_max_dst < D[u][v]:
                curr_max_dst = D[u][v]
        if -float('inf') < curr_max_dst < max_dst:
            br, max_dst = v, curr_max_dst

    return br, max_dst


if __name__ == "__main__":
    print(best_root([[-1, 2, 10, 3, -1],
                     [2, -1, -1, -1, -1],
                     [10, -1, -1, -1, 150],
                     [3, -1, -1, -1, -1],
                     [-1, -1, 150, -1, -1]]))
