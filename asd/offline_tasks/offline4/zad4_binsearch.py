from zad4testy import runtests
import time

def select_buildings(T, p):
    n = len(T)

    T.append((0, 0, -float('inf'), 0))
    ind = [i for i in range(n + 1)]
    ind.sort(key=lambda i: T[i][2])
    
    F = [[0 for _ in range(p + 1)] for _ in range(n + 1)]
    save_prevs = [0 for _ in range(n + 1)]

    for building in range(1, n + 1):
        h, a, b, w = T[ind[building]]

        save_prevs[building] = first_non_colliding_building(T, ind, building, a)

        for price in range(p+1):
            F[building][price] = F[building - 1][price]
            if price - w >= 0:
                F[building][price] = max(F[building][price], F[save_prevs[building]][price - w] + (b - a) * h)

    result = []
    building, price = n, p
    while building > 0 and price >= 0:
        if F[building - 1][price] == F[building][price]:
            building -= 1
        else:
            result.append(ind[building])
            price -= T[ind[building]][3]
            building = save_prevs[building]
    return result


def first_non_colliding_building(T, ind, right, a):
    left = 1
    while left <= right:
        mid = int((left + right) / 2)
        prev_mid_b, mid_b = T[ind[mid - 1]][2], T[ind[mid]][2]

        if prev_mid_b < a <= mid_b:
            return mid - 1
        elif mid_b < a:
            left = mid + 1
        else:
            right = mid - 1

    return  0

    
runtests(select_buildings)
