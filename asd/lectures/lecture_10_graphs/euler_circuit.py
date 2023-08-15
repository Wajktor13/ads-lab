def DFS_Euler_circuit(G):

    if not Euler_circuit_exists(G):
        return None

    def DFS_visit(v, s):
        visited_edges[v][s] = visited_edges[s][v] = True
        visited[s] = True

        for i in range(len(G[s])):
            if not visited_edges[G[s][i]][s]:
                DFS_visit(s, G[s][i])
        result.append(s)

    result = []
    n = len(G)
    visited = [False for _ in range(n)]
    visited_edges = [[False for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for u in range(len(G[v])):
            if not visited_edges[v][G[v][u]]:
                visited[v] = True
                DFS_visit(v, G[v][u])
                result.append(v)
        
        if not all(visited):
            #graph is not consistent
            return None
   
    return result


def Euler_circuit_exists(G):
    for v in G:
        if len(v) % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    print(DFS_Euler_circuit([[3, 4], [2, 4], [1, 4], [0, 4], [1, 2, 0, 3]]))
