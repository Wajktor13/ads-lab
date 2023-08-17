"""
czy można przejść z s do e po malejących wagach?

można przerabiać wierzchołki na krawędzie i na odwrót
"""


from collections import deque


def can_reach_by_decreasing_weights(G, W, x, y):
    n = len(G)
    starting_edges, ending_edges = [], []
    
    converted_G = convert(G)

    for v in G[x]:
        starting_edges.append((x, v) if x < v else (v, x))
    for v in G[y]:
        ending_edges.append((y, v) if y < v else (v, y))

    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]    
    for se in starting_edges:
        if visited[se[0]][se[1]]:
            continue
        Q = deque()
        Q.append(se)

        while Q:
            v1, v2 = Q.popleft()
            for u1, u2 in converted_G[v1][v2]:
                if not visited[u1][u2] and W[u1][u2] < W[v1][v2]:
                    visited[u1][u2] = True
                    parent[u1][u2] = (v1, v2)
                    Q.append((u1, u2))
        
        for v1, v2 in ending_edges:
            if visited[v1][v2]:
                return True, get_result(parent, v1, v2)
    
    return False, []


#converts edges to vertices and vice versa
def convert(G):
    n = len(G)
    converted_G = [[[] for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for s in G[v]:
            if s < v:
                continue

            for u in G[v]:
                if u != s:
                    converted_G[v][s].append((v, u) if v < u else (u, v))
            for u in G[s]:
                if u != v:
                    converted_G[v][s].append((s, u) if s < u else (u, s))
    
    return converted_G


def get_result(parent, v1, v2):
    path_edges= []
    get_path(parent, path_edges, v1, v2)
    path_edges.reverse()

    path_vertices = [None for _ in range(len(path_edges) + 1)]
    
    for i in range(1, len(path_edges)):
        if path_edges[i - 1][1] != path_edges[i][0]:
            path_edges[i] = (path_edges[i][1], path_edges[i][0])
        path_vertices[i] = path_edges[i][0]

    path_vertices[0], path_vertices[-1] = path_edges[0][0], path_edges[-1][1]

    return path_edges, path_vertices


def get_path(parent, path, v1, v2):
    path.append((v1, v2))
    if parent[v1][v2] is not None:
        get_path(parent, path, parent[v1][v2][0], parent[v1][v2][1])


if __name__ == '__main__':
    print(can_reach_by_decreasing_weights([[1, 2, 4], [0, 4, 5], [5, 3, 4, 0], [2, 4], [0, 1, 2, 3], [2, 1]],
                                          [[0, 11, 1, 5, 0, 0],
                                           [0, 0, 0, 0, 8, 20],
                                           [0, 0, 0, 3, 10, 2],
                                           [0, 0, 0, 0, 6, 0],
                                           [0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0]], 0, 5))
