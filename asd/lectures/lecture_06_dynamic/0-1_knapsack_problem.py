def knapsack_problem(weights, prices, max_weight):
    n = len(weights)
    F = [[0 for _ in range(max_weight + 1)] for _ in range(n)]
    for w in range(weights[0], max_weight + 1):
        F[0][w] = prices[0]

    for w in range(max_weight+1):
        for i in range(1, n):
            F[i][w] = F[i-1][w]
            if w - weights[i] >= 0:
                F[i][w] = max(F[i][w], F[i-1][w - weights[i]] + prices[i])

    return [F[n - 1][max_weight]] + get_knapsack(F, weights, prices, max_weight)


def get_knapsack(F, weights, prices, max_weight):
    n = len(weights)
    knapsack = []
    total_weight = 0
    i, w = n - 1, max_weight
    while F[i][w] != 0 and i >= 0:
        if w - weights[i] >= 0 and F[i - 1][w - weights[i]] + prices[i] == F[i][w] or i == 0:
            knapsack.append(i)
            total_weight += weights[i]
            w -= weights[i]
        i -= 1

    return [total_weight, knapsack[::-1]]


if __name__ == "__main__":
    print(knapsack_problem(
        [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13],
        [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312],
        850))
