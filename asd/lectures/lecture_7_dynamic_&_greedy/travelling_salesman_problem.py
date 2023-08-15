def tsp(distance):
    n = len(distance)
    last_bitmask = (2 ** n) - 1
    F = [[None for _ in range(last_bitmask + 1)] for _ in range(n)]
    F[0][1] = 0
    
    best = float('inf')
    for end in range(1, n):
        best = min(best, fill(F, distance, end, last_bitmask) + distance[0][end])

    return best


def fill(F, distance, row, col):
    if F[row][col] is not None:
        return F[row][col]
    
    F[row][col] = float('inf')
    cities = get_cities(col)
    
    for city in cities:
        if city != row and col - 2 ** row >= 0:
            F[row][col] = min(F[row][col], fill(F, distance, city, col - 2 ** row) + distance[row][city])
    return F[row][col]


def get_cities(bitmask):
    result = []
    city = 0
    num = bitmask

    while num > 0:
        if num % 2:
            result.append(city)

        num //= 2
        city += 1

    return result


if __name__ == '__main__':
    print(tsp([[0, 7, 3],
               [7, 0, 2], 
               [3, 2, 0], ]))

    print(tsp([[0, 1, 5, 5],
               [1, 0, 20, 9], 
               [5, 20, 0, 2], 
               [5, 9, 2, 0]]))
    
    print(tsp([[0, 3, 4, 1, 7],
               [3, 0, 2, 1, 9], 
               [4, 2, 0, 3, 19], 
               [1, 1, 3, 0, 5],
               [7, 9, 19, 5, 0]]))
