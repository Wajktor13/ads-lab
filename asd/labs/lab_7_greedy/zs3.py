"""
zbior ladunkow - potegi 2: [2, 4, 2, 8, 32] - 2^k
mamy ciezarowke z max poj
chcemy wziac max wage sumaryczna

bierzemy najwiekszy

jak problem z wydawaniem reszty
"""


def send(T, W):
    T.sort(reverse=True)
    result = []
    while T:
        if T[0] < W:
            result.append(T.pop(0))
            W -= result[-1]
        else:
            T.pop(0)
    return result
    