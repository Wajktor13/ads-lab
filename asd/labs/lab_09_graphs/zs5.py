def min_groups(G, K, A, B):
    n = find_no_of_vertices(G)
    min_capacity = [-float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    min_capacity[A] = K

    for _ in range(n - 1):
        for x, y, c in G:
            if min_capacity[y] < min(min_capacity[x], c):
                min_capacity[y] = min(min_capacity[x], c)
                parent[y] = x
            
            if min_capacity[x] < min(min_capacity[y], c):
                min_capacity[x] = min(min_capacity[y], c)
                parent[x] = y
    
    route = []
    get_route(parent, route, B)

    return K // min_capacity[B] if K % min_capacity[B] == 0 else K // min_capacity[B] + 1, route[::-1]
    

def find_no_of_vertices(G):
    n = -float('inf')
    for x, y, c in G:
        n = max(n, x, y)
    return n + 1


def get_route(parent, route, v):
    route.append(v)
    if parent[v] is not None:
        get_route(parent, route, parent[v])


if __name__ == "__main__":
    print(min_groups([(0, 1, 15), (0, 3, 5), (0, 5, 10), (1, 2, 12), (5, 4, 3), (3, 2, 15),
                      (3, 4, 1), (3, 6, 10), (2, 6, 4), (4, 6, 2)], 22, 0, 6))
