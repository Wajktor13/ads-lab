def max_height(A): # [(a, b), ...]
    A = [(-float('inf'), float('inf'))] + A
    n = len(A)
    F = [-float('inf') for _ in range(n)]
    save = [None for _ in range(n)]

    F[0], save[0] = 0, 0

    max_h, last_tower_ind = 0, 0

    for i in range(1, n):
        tower = A[i]
        for j in range(1, i + 1):
            prev_tower = A[i - j]
            if prev_tower[0] <= tower[0] and prev_tower[1] >= tower[1] and F[i - j] + 1 > F[i]:
                F[i] = F[i - j] + 1
                save[i] = j

                if F[i] > max_h:
                    max_h = F[i]
                    last_tower_ind = i
    
    return max_h, get_towers(save, last_tower_ind)

def get_towers(save, last):
    result = []
    tower = last

    while save[tower] > 0:
        result.append(tower - 1)
        tower -= save[tower]
    
    return sorted(result)


if __name__ == "__main__":
    print(max_height([(1, 8), (2, 7), (4, 9), (3, 6), (3, 7), (4, 5), (4, 5), (0, 10)]))
