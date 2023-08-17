def knapsack(A, P, c):
    n = len(A)
    capacity_left = c

    ind = [i for i in range(n)]
    price_to_volume = [P[i] / A[i] for i in range(n)]
    ind.sort(key=lambda i: price_to_volume[i], reverse=True)

    result = []
    i = 0
    while capacity_left > 0:
        to_take = min(capacity_left, A[ind[i]])
        result.append((ind[i], f'{round(to_take / A[ind[i]] * 100, 2)}%'))
        capacity_left -= to_take
        i += 1

    return result


if __name__ == '__main__':
    print(knapsack([2, 3, 7, 3, 2], [1, 2, 6, 15, 4], 10))