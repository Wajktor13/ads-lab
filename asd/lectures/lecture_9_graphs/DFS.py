def DFS(G):

    def DFS_visit(v):
        nonlocal current_time
        current_time += 1
        visited[v], visit_time[v] = True, current_time

        for s in G[v]:
            if not visited[s]:
                parent[s] = v
                DFS_visit(s)
        done_time[v]  = current_time
        current_time += 1
        

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visit_time = [None for _ in range(n)]
    done_time = [None for _ in range(n)]
    current_time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)
