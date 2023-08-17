"""
mamy sieć autostrad - graf
każda krawędź ma przydzielony koszt 0/1
szukamy najmniejszego kosztu

1 - hiperwierzchołki

2 - bfs, 2 kolejki, jedna na darmowe, druga na płatne, 2x visited 
dla innych wartości niz 0/1 krawędź o wartości np 3 zamieniamy na 3 krawędzie o wart 1

"""


from collections import deque


def cheapest_route(G, s, t):
    n = len(G)
    visited_free = [False for _ in range(n)]
    visited_toll = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    free_Q, toll_Q = deque(), deque()

    free_Q.append(s)
    visited_free[s] = visited_toll[s] = True

    while free_Q or toll_Q:
        while free_Q:
            v = free_Q.popleft()
            for u in range(n):
                print(u, v)
                if G[v][u] >= 0 and not visited_free[u]:
                    parent[u] = v
                    if G[v][u] == 0:
                        visited_free[u] = True
                        free_Q.append(u)
                    else:
                        visited_toll[u] = True
                        toll_Q.append(u)
        
        while toll_Q:
            v = toll_Q.popleft()
            for u in range(n):
                if G[v][u] >= 0 and not (visited_free[u] or visited_toll[u]):
                    parent[u] = v
                    if G[v][u] == 0:
                        visited_free[u] = True
                        free_Q.append(u)
                    else:
                        visited_toll[u] = True
                        toll_Q.append(u)
    
    if visited_free[t] or visited_toll[t]:
        route = []
        get_route(route, parent, t)
    
    return route[::-1]


def get_route(route, parent, v):
    if v is not None:
        route.append(v)
        get_route(route, parent, parent[v])
        

if __name__ == "__main__":
    print(cheapest_route([[-1, 0, 0, -1, -1, 1, -1, -1],
                          [-1, -1, 1, 1, -1, -1, -1, -1],
                          [-1, -1, -1, -1, 0, -1, -1, -1],
                          [-1, -1, -1, -1, -1, 0, 0, -1],
                          [-1, -1, -1, 0, -1, -1, 1, -1],
                          [-1, -1, -1, -1, -1, -1, 1, -1],
                          [-1, -1, -1, -1, -1, -1, -1, 0],
                          [-1, -1, -1, -1, -1, -1, -1, -1]], 0, 7))
                          