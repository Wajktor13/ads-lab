"""Wiktor Wilkusz 411605
Algorytm dla każdej krawędzi sprawdza, czy istnieje MST, w którym najmniejszą
wagą jest waga tej krawędzi. Jeśli tak, to sprawdza czy różnica między największą
wagą w znalezionym MST a wagą rozważanej krawędzi jest mniejsza niż min_diff.
Jeśli tak, to min_diff jest aktualizowany.

MST jest znajdowany za pomocą algorytmu Kruskala.
"""

from zad8testy import runtests


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
         return

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y

        if x.rank == y.rank:
            y.rank += 1


def ceil(num):
    if int(num) == num:
        return int(num)
    else:
        return int(num) + 1


def build_graph(A):
    """
    returns graph represented by list with edges
    """
    n = len(A)
    G = []
    for i in range(n - 1):
        for j in range(i+1, n):
            xi, yi = A[i]
            xj, yj = A[j]
            w = ceil(((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5)
            G.append((i, j, w))
    return G 


def highway( A ):
    V = len(A)
    G = build_graph(A)
    n = len(G)
    G.sort(key=lambda e: e[2])
    min_diff = float('inf')

    for i in range(n - V + 1):
        u1, v1, w1 = G[i]

        visited = [False for _ in range(V)]
        sets = [Node(i) for i in range(V)]

        visited[u1] = visited[v1] = True
        union(sets[u1], sets[v1])
        diff = float('inf')

        for j in range(i + 1, n):
            u2, v2, w2 = G[j]
            if find(sets[u2]) != find(sets[v2]):
                diff = w2 - w1

                if diff >= min_diff:
                    break

                visited[u2] = visited[v2] = True
                union(sets[u2], sets[v2])
        
        if all(visited):
            min_diff = min(min_diff, diff)

    return min_diff


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
