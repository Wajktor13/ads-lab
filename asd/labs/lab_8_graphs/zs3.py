from collections import deque


def shortes_weighted_path_BFS(G, s, e):  # G = [[(v, weight)]]
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    Q.append((s, 0, 0, None))  # (v, to_go, init, parent)

    while Q:
        v, to_go, init, p = Q.popleft()

        if visited[v]:
            continue

        if to_go == 0:
            visited[v] = True
            distance[v] = init
            parent[v] = p
            for s, w in G[v]:
                if not visited[s]:
                    Q.append((s, w - 1, distance[v] + w, v))
        else:
            Q.append((v, to_go - 1, init, p))

    route = []
    get_route(parent, route, e)

    return distance[e], route[::-1]


def get_route(parent, route, v):
    route.append(v)
    if parent[v] is not None:
        get_route(parent, route, parent[v])


if __name__ == "__main__":
    print(shortes_weighted_path_BFS([[(1, 11), (3, 1), (4, 2)], [(0, 11), (2, 3), (4, 10)], [(4, 1), (1, 3)],
                                     [(0, 1), (4, 8)], [(2, 1), (1, 10), (0, 2), (3, 8)]], 3, 1))
    