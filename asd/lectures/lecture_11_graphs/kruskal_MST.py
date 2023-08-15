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


def count_vertices(G):
    n = 0
    for e in G:
        n = max(n, e[0][0], e[0][1])
    return n + 1


def kruskal_MST(G): # G:=[((x, y), w)]
    n = count_vertices(G)
    mst = []
    sets = []
    for i in range(n):
        sets.append(Node(i))
    
    G.sort(key=lambda e: e[1])

    for e in G:
        u, v = e[0]
        if find(sets[u]) != find(sets[v]):
            union(sets[u], sets[v])
            mst.append((u, v))
    
    return mst


########################################################################################
def simplified_kruskal_MST(G): # G:=[((x, y), w)]
    n = count_vertices(G)
    parent = [i for i in range(n)]
    mst = []

    G.sort(key=lambda e: e[1])

    for e in G:
        u, v = e[0]
        if parent[u] != parent[v]:
            mst.append((u, v))
            for i in range(n):
                tmp = parent[u]
                if parent[i] == tmp:
                    parent[i] = parent[v]
                    
    return mst
