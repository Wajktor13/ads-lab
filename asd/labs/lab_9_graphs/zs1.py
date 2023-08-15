"""
np-trudne dla dowolnego grafu
dla dag nie jest np trudny

sortowanie topologiczne, przejscie od 0 i sprawdzenie czy all visited
"""

from collections import deque


def topological_sort(G):

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


def Hamiltonian_path_DAG(G):
    n = len(G)
    top_sorted = topological_sort(G)

    for i in range(n-1):
        if top_sorted[i+1] not in G[top_sorted[i]]:
            return []

    return top_sorted


if __name__ == "__main__":
    print(Hamiltonian_path_DAG([[1, 4], [2, 4], [], [0, 4], [2]]))
    print(Hamiltonian_path_DAG([[1, 4], [2, 4], [], [0], [2, 3]]))
    print(Hamiltonian_path_DAG([[1, 4], [2, 4], [], [0, 4], [2], [6], []]))
    