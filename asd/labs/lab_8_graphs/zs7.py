from collections import deque


def kings_path(A):
    n = len(A)
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[None for _ in range(n)] for _ in range(n)]
    parent = [[(None, None) for _ in range(n)] for _ in range(n)]
    Q = deque()

    Q.append(((0, 0), 0, 0, (None, None))) # ((row, col), to_go, init, (prow, pcol))

    while len(Q) > 0:
        coords, to_go, init, parentcoords = Q.popleft()
        row, col = coords

        if visited[row][col]:
            continue

        elif to_go > 0:
            Q.append(((coords), to_go - 1, init, (parentcoords)))

        else:
            visited[row][col] = True
            distance[row][col] = init
            parent[row][col] = parentcoords
            neighbours = get_neighbours(n, row, col)

            for nrow, ncol in neighbours:
                if not visited[nrow][ncol]:
                    Q.append(((nrow, ncol), A[nrow][ncol] - 1, init + A[nrow][ncol], (row, col)))
    
    return distance[n - 1][n - 1], get_route(parent)
    

def get_neighbours(n, row, col):
    neighbours = []

    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    
    if row + 1 < n:
        neighbours.append((row + 1, col))

    if  col - 1 >= 0:
        neighbours.append((row, col - 1))
    
    if col + 1 < n:
        neighbours.append((row, col + 1))
    
    return neighbours


def get_route(parent):
    n = len(parent)
    route = [[0 for _ in range(n)] for _ in range(n)]
    row, col = n - 1, n - 1

    while row is not None:
        route[row][col] = 1
        row, col = parent[row][col]
    
    return route


if __name__ == "__main__":
    d, r = kings_path([[0, 1, 13, 4, 4, 2],
                       [1, 33, 11, 2, 11, 4],
                       [2, 0, 1, 1, 18, 1],
                       [11, 11, 12,17, 13, 9],
                       [2, 1, 2, 22, 15, 2],
                       [11, 12, 7, 26, 3, 1]])

    print(d)

    for row in r:
        print(row)
