from collections import deque


def can_reach(G, t, x, y):
    n = len(G)
    ceilings = []
    for v, w in G[x]:
        for diff in range(t + 1):
            if w - diff > 0:
                ceilings.append(w - diff)
            ceilings.append(w + diff)

    ceilings = unique(ceilings)

    for c in ceilings:
        visited = [False for _ in range(n)]
        parents = [None for _ in range(n)]
        Q = deque()

        visited[x] = True
        Q.append(x)

        while Q:
            v = Q.popleft()
            for s, w in G[v]:
                if not visited[s] and abs(w - c) <= t:
                    visited[s] = True
                    parents[s] = v
                    Q.append(s)
        
        if visited[y]:
            route = []
            get_route(route, parents, y)

            return True, route[::-1], c
    
    return False, [], None


def unique(A):
    result = []
    i = 0
    n = len(A)

    A.sort()
    
    while i < n:
        result.append(A[i])
        i += 1
        while i < n and A[i - 1] == A[i]:
            i += 1
    
    return result


def get_route(route, parents, v):
    if v is not None:
        route.append(v)
        get_route(route, parents, parents[v])


if __name__ == "__main__":
    print(can_reach([[(3, 5), (2, 3), (1, 1)], [(0, 1), (4, 8)], [(0, 3), (3, 15), (4, 10)],
                     [(0, 5), (2, 15), (4, 100)], [(1, 8), (2, 10), (3, 100), (6, 100), (5, 6)],
                     [(6, 4), (4, 6)], [(5, 4), (4, 100)]], 5, 0, 6))
