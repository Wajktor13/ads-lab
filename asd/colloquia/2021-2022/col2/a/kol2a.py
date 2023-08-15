from kol2atesty import runtests

JACEK = 0
MARIAN = 1
CONTROL_POINT = False


def drivers( P, B ):
    n = len(P)
    F = [[None, None] for _ in range(n)]

    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda station: station[0])

    fill(P, B, F, 0, 0)

    return get_result(P, B, F)


def fill(P, B, F, point, driver):
    if F[point][driver] is not None:
        return F[point][driver]
    
    n = len(P)
    count_control_points = count_change_points = 0
    F[point][driver] = float('inf')

    for i in range(point + 1, n):
        if i == n - 1 or P[i][0] == B:
                if driver == MARIAN:
                    if P[i][1] == CONTROL_POINT:
                        count_control_points += 1
                    F[point][driver] = min(F[point][driver], count_control_points)
                else:
                    F[point][driver] = 0
                break

        if P[i][1] == CONTROL_POINT:
            count_control_points += 1
        else:
            count_change_points += 1 

            if driver == JACEK:
                F[point][JACEK] = min(F[point][JACEK], fill(P, B, F, i, MARIAN))
            else:
                F[point][MARIAN] = min(F[point][MARIAN], fill(P, B, F, i, JACEK) + count_control_points)

            if count_change_points == 3:
                break
    
    return F[point][driver]


def get_result(P, B, F):
    n = len(P)
    driver = JACEK
    point, i = 0, 1
    count_control_points = 0
    result = []

    while i < n and P[i][0] < B:
        if P[i][1] == CONTROL_POINT:
            count_control_points += 1
        else:
            if driver == JACEK and F[point][JACEK] == F[i][MARIAN]:
                result += [P[i][2]]
                point = i
                count_control_points = 0
                driver = MARIAN

            elif driver == MARIAN and F[point][MARIAN] == F[i][JACEK] + count_control_points:
                result += [P[i][2]]
                point = i
                count_control_points = 0
                driver = JACEK
        i += 1
    
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
