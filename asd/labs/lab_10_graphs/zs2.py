def hamiltonian_cycle(G):
    n = len(G)
    visited = [False for _ in range(n)]

    return goto(G, visited, 0, 0)


def goto(G, visited, start, v):
    visited[v] = True

    if all(visited) and start in G[v]:
        return True
    
    for u in G[v]:
        if not visited[u]:
            if goto(G, visited, start, u):
                return True
            visited[u] = False
    
    return False


if __name__ == "__main__":
    print(hamiltonian_cycle([[3, 2], [4], [0, 3], [2, 0, 4, 5], [1, 3, 5], [3, 4]]))
    print(hamiltonian_cycle([[1, 3, 2], [0, 4], [0, 3], [2, 0, 4, 5], [1, 3, 5], [3, 4]]))
    