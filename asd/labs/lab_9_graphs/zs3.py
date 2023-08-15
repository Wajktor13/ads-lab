def shortest_path_DAG(G, s):
    n = len(G)
    distance = [float('inf') for _ in range(n)]

    distance[s] = 0
    tsorted = topological_sort(G)
    tsorted = tsorted[tsorted.index(s):]

    for v in tsorted:
        for u, w in G[v]:
            if distance[u] > distance[v] + w:
                distance[u] = distance[v] + w
    
    return distance
    

def topological_sort(G):

    def DFS_visit(v):

        visited[v] = True

        for s, w in G[v]:
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


if __name__ == "__main__":
    print(shortest_path_DAG([[(1, 11), (4, 2)], [(2, 3)], [], [(0, 1), (4, 8)], [(1, 10), (2, 1)]], 3))
    print(shortest_path_DAG([[(1, 11), (4, 2)], [(2, 3)], [], [(0, 1), (4, 8)], [(1, 10), (2, 1)]], 0))
    