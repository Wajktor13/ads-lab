def strongly_connected_components(G):
    n = len(G)
    G_T = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    scc = []

    for v in range(n):
        for s in G[v]:
            G_T[s].append(v)

    processed_times = DFS_find_processed_times(G)
    ordered_Vs = [i for i in range(n)]
    ordered_Vs.sort(key=lambda v: - processed_times[v])

    for v in ordered_Vs:
        if not visited[v]:
            component = []
            DFS_visit_component(G_T, v, visited, component)
            scc.append(component)

    return scc
        
        
def DFS_find_processed_times(G):

    def DFS_visit(v):
        nonlocal current_time
        visited[v] = True

        for s in G[v]:
            if not visited[s]:
                DFS_visit(s)
        processed_time[v]  = current_time
        current_time += 1
        

    n = len(G)
    visited = [False for _ in range(n)]
    processed_time = [None for _ in range(n)]
    current_time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)
    
    return processed_time


def DFS_visit_component(G, v, visited, component):
    visited[v] = True

    for s in G[v]:
        if not visited[s]:
            DFS_visit_component(G, s, visited, component)

    component.append(v)
