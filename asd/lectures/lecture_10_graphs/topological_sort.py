def DFS_topological_sort(G):

    def DFS_visit(v):

        visited[v] = True

        for s in G[v]:
            if not visited[s]:
                DFS_visit(s)
        result.append(v)
        
    result = []
    n = len(G)
    visited = [False for _ in range(n)]

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)

    return result[::-1]
