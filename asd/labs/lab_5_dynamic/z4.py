"""
mamy ciag macierzy 
M1, M2, ... Mn
znalezc optymalny koszt mnozenia macierzy
nawiasy, nie kolejnosc

dla 4 macierzy: mamy 3 mozliwosci pierwszego mnozenia

koszt pomnozenia 2 macierzy: m1.rows * m2.cols * m2.rows
przy czym m1.cols == m2.rows

dla pojedynczej koszt 0

od i-tej do j-tej:
f(M, i, j) = 0, i == j
           = min (f(M, i, k) + f(M, k+1, j) + g(M, i, j, k)), wpp
          k = i -> j:

g - koszt mnozenia

najtrudniej zapisac funkcje mat.
"""


def min_multip_cost(m):
    n = len(m)
    costs = [[float('inf') for _ in range(n)] for _ in range(n)]
    save_splits = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        costs[i][i] = 0
        for j in range(i + 1, n):
            for k in range(i, j):
                k_split_cost = costs[i][k] + costs[k + 1][j] + m[i][0] * m[j][1] * m[k][1]
                if k_split_cost < costs[i][j]:
                    costs[i][j] = k_split_cost
                    save_splits[i][j] = k

    return costs[0][n - 1], put_brackets(save_splits, 0, n - 1)


def put_brackets(splits, i, j):
    if i == j:
        return f'M{i}'
    if i + 1 == j:
        return f'M{i}M{j}'
    else:
        k = splits[i][j]
        return f'({put_brackets(splits, i, k)})({put_brackets(splits, k + 1, j)})'


if __name__ == "__main__":
    print(min_multip_cost([[30, 35], [35,15], [15,5], [5,10], [10, 20], [20, 25]]))
    