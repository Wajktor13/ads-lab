def DFS_articulation_points(G):
    def DFS_visit(v):
        nonlocal current_time

        visited[v] = True
        time[v] = low[v]  = current_time
        current_time += 1

        for s in G[v]:
            if visited[s] and v not in child[s]:
                low[v] = min(low[v], low[s])
            elif not visited[s]:
                parent[s] = v
                child[v].append(s)
                DFS_visit(s)

        for c in child[v]:
            low[v] = min(low[v], low[c])

        for c in child[v]:
            if low[c] >= time[v] and parent[v] is not None:
                articulation_points.append(v)
                break

    n = len(G)
    visited = [False for _ in range(n)]
    time = [None for _ in range(n)]
    low = [None for _ in range(n)]
    child = [[] for _ in range(n)]
    parent = [None for _ in range(n)]
    articulation_points = []
    current_time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)
    
    if parent.count(0) >= 2:
        articulation_points.append(0)

    return articulation_points
