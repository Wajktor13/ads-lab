"""
Sieci telekomunikacyjne reprezentowane jako graf
aby porozmawiać trzeba byc w tej samej spójnej składowej

wyłączamy stacje w takiej kolejności, aby graf się nie rozspójnił - czyli aby nie 
przerwać nikomu połaczenia - musi istnieć połączenie między każdymi pozostałymi stacjami

przechodzimy dfs i jesli spotkamy odwiedzony v, to usuwamy daną krawędź

w dfs mozna zliczać 2 rodzaje czasu - czas wrzucenia na stos i czas przetworzenia
preorder i postorder

3 stany - logika 3-wart

dopuszczalne przez O zmienne globalne typu: 
IN_PROGRESS = 1
DONE = 2
(coś jak preprocesor w C)

bfs - tworzymy drzewo ścieżek parent-child i usuwamy od liści - dfs łatwiejszy


#bfs ps
q = queue()
children = [0, 0...]
q.put(0)
while q:
    u = q.pop()
    for neig of u:
        children[u] += 1
        parents[neig] = u
        q.put(neig)
"""


from queue import Queue


# BFS
def delete_queue1(G):
    V = len(G)
    visited = [False for _ in range(V)]
    childs = [[] for _ in range(V)]
    Q = Queue()

    visited[0] = True
    Q.put(0)

    while not Q.empty():
        u = Q.get()
        for s in G[u]:
            if not visited[s]:
                visited[s] = True
                childs[u].append(s)
                Q.put(s)

    del_q = []
    fill_del_q(del_q, childs, 0)
    
    return del_q


def fill_del_q(del_q, childs, v):
    if childs[v] == []:
        del_q.append(v)
    else:
        for i in range(len(childs[v])):
            c = childs[v][i]
            fill_del_q(del_q, childs, c)
        del_q.append(v)


#DFS
def delete_queue2(G):
    V = len(G)
    visited = [False for _ in range(V)]
    del_q = []

    for v in range(V):
        if not visited[v]:
            stack = [v]
            while stack:
                u = stack.pop()
                if not visited[u]:
                    del_q.append(u)
                    visited[u] = True
                    for s in G[u]:
                        if not visited[s]:
                            stack.append(s)


    return del_q[::-1]


if __name__ == '__main__':
    connected_graph = [[1, 2, 6], [0, 5, 2], [0, 3, 1], [2, 4, 7], [3, 7, 5, 9],
     [1, 4, 6], [0, 5], [3, 4, 8], [7], [4]]
    
    unconnected_graph = [[1, 2, 6], [0, 5, 2], [0, 3, 1], [2, 4, 7], [3, 7, 5, 9],
     [1, 4, 6], [0, 5], [3, 4, 8], [7], [4], [11], [12, 13], [11, 13], [11, 12]] #

    print(delete_queue1(connected_graph))
    print(delete_queue2(unconnected_graph))
    