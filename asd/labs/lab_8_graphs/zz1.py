def captain_problem(M, T):
    n, m = len(M), len(M[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    parents = [[None for _ in range(m)] for _ in range(n)]

    DFS_visit(M, T, visited, parents, 0, 0)
    
    if visited[n - 1][m - 1]:
        path = [[0 for _ in range(m)] for _ in range(n)]
        get_path(M, parents, path, n - 1, m - 1)

        return True, path
    
    return False, [[]]


def DFS_visit(M, T, visited, parents, row, col):
    n, m = len(M), len(M[0])
    visited[row][col] = True

    if row - 1 >= 0 and M[row - 1][col] > T and not visited[row - 1][col]:
        DFS_visit(M, T, visited, parents, row - 1, col)
        parents[row - 1][col] = (row, col)
    
    if col + 1 < m and M[row][col + 1] > T and not visited[row][col + 1]:
        DFS_visit(M, T, visited, parents, row, col + 1)
        parents[row][col + 1] = (row, col)
    
    if row  + 1 < n and M[row + 1][col] > T and not visited[row + 1][col]:
        DFS_visit(M, T, visited, parents, row + 1, col)
        parents[row + 1][col] = (row, col)
    
    if col - 1 >= 0 and M[row][col - 1] > T and not visited[row][col - 1]:
        DFS_visit(M, T, visited, parents, row, col - 1)
        parents[row][col - 1] = (row, col)


def get_path(M, parents, path, row, col):
    path[row][col] = 1
    if parents[row][col] is not None:
        get_path(M, parents, path, parents[row][col][0], parents[row][col][1])
    

if __name__ == "__main__":
    result, route = captain_problem([[0, 6, 3, 5, 1, 2],
                                     [3, 7, 0, 7, 8, 9],
                                     [0, 8, 0, 9, 1, 6],
                                     [0, 9, 7, 8, 2, 9],
                                     [1, 0, 1, 3, 4, 8],
                                     [2, 3, 0, 0, 2, 6]], 5)
    
    for row in route:
        print(row)
