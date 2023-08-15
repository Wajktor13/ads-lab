"""
Czy graf jest dwudzielny?
k-dzielnosc

przechodzimy po wszystkich v i nadajemy jedna z 2 wartosci, O(V + E)

3 algorytm obok dfs i bfs - a-star? - nie zawsze dziala
"""

from queue import Queue


def is_bipartite(G):
    V = len(G)
    visited = [False for _ in range(V)]
    value = [0 for _ in range(V)]

    Q = Queue()
    visited[0] = True
    Q.put(0)

    while not Q.empty():
        u = Q.get()

        for s in G[u]:
            if visited[s] and value[s] == value[u]:
                return False
            if not visited[s]:
                visited[s] = True
                value[s] = (value[u] + 1) % 2                   
                Q.put(s)
    
    return True


if __name__ == "__main__":
    print(is_bipartite([[3, 4, 5], [4], [4, 5], [0], [0, 1, 2], [0, 2]]))
