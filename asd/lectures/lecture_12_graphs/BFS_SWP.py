from collections import deque


def shortes_weighted_path_BFS(G): # G = [[(v, weight)]]
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    Q = deque()
    Q.append((0, 0, 0)) # (v, to_go, init)

    while Q:
        v, to_go, init = Q.popleft()
        
        if visited[v]:
            continue

        if to_go == 0:
            visited[v] = True
            distance[v] = init
            for s, w in G[v]:
                if not visited[s]:
                    Q.append((s, w - 1, distance[v] + w))
        else:
            Q.append((v, to_go - 1, init))
    
    return distance
        