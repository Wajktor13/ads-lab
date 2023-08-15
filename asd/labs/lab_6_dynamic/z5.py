"""
2 wym problem plecakowy
rzeczy w pudelkach o roznych wagach
ukladamy jedno na drugie
obciazenie max x kg i wieza moze miec max y cm

to samo co zwykle plecakowe ale dochodzi jeden wymiar na wysokosc

f(P, w, h, i) = 0, w <= 0 or h <= 0
              = max(f(P, w, h, i+1), f(P, w-P[i].weight, h - P[i].height, i + 1) + P[i].value)
              i < n


class Item:
    value
    weight
    height
"""


def two_dim_knapsack_problem(v, w, h, W, H):
    v, w, h = [0] + v, [0] + w, [0] + h, 
    n = len(v)
    F = [[[None for _ in range(H + 1)] for _ in range(W + 1)] for _ in range(n)]
    save = [[[None for _ in range(H + 1)] for _ in range(W + 1)] for _ in range(n)]

    fill(F, v, w, h, n - 1, W, H, save)

    return F[n - 1][W][H], get_result(save, n, W, H)


def fill(F, v, w, h, ii, wi, hi, save):
    if not all((ii, wi, hi)):

        F[ii][wi][hi] = 0
        save[ii][wi][hi] = (False, ii - 1, wi, hi)

    elif F[ii][wi][hi] is None:

        F[ii][wi][hi] = fill(F, v, w, h, ii - 1, wi, hi, save)
        save[ii][wi][hi] = (False, ii - 1, wi, hi)

        if wi - w[ii] >= 0 and hi - h[ii] >= 0 and\
                F[ii][wi][hi] < fill(F, v, w, h, ii - 1, wi - w[ii], hi - h[ii], save)\
                + v[ii]:

            F[ii][wi][hi] = F[ii -1][wi - w[ii]][hi - h[ii]] + v[ii]
            save[ii][wi][hi] = (True, ii - 1, wi - w[ii], hi - h[ii])

    return F[ii][wi][hi]


def get_result(save, n, W, H):
    ii, wi, hi = n - 1, W, H
    result = []

    while ii > 0:
        take, ii, wi, hi = save[ii][wi][hi]
        if take:
            result.append(ii)

    return result[::-1]


if __name__ == '__main__':
    prices = [1, 7, 3, 2]
    weights = [2, 13, 5, 5]
    heights = [2, 2, 7, 1]
    max_weight, max_height = 20, 9
    print(two_dim_knapsack_problem(prices, weights, heights, max_weight, max_height))
    