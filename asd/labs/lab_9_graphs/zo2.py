from queue import PriorityQueue


def KruskalMST(G): #G:=[(u, v, w)]
    n = 0
    for e in G:
        n = max(n, max(e[0], e[1])) #znajduje max wierzcholek
    n = n + 1

    PQ = PriorityQueue() #zamiast sortowania tablicy
    
    for e in G:
        PQ.put((e[2], (e[0], e[1])))

    sets = [i for i in range(n)]
    edges = []

    while not PQ.empty():
        e = (PQ.get())[1]
        x, y = e
        if sets[x] != sets[y]: #find
            edges.append(e)         
            tmpy = sets[y]                #
            for i in range(n):            # union
                if sets[i] == tmpy:       #
                    sets[i] = sets[x]     #

    return edges


if __name__ == "__main__":
    print(KruskalMST([(0, 1, 11), (0, 3, 1), (0, 4, 2), (1, 4, 10), (1, 2, 3), (3, 4, 8), (2, 4, 1)]))
    