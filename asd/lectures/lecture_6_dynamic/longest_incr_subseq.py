def lis(A):
    n = len(A)
    max_ind = 0
    F = [1 for _ in range(n)]
    indieces = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                indieces[i] = j
                F[i] = F[j] + 1

        if F[i] > F[max_ind]:
            max_ind = i
    
    return F[max_ind], get_subseq(A, F, indieces, max_ind)


def get_subseq(A, F, indieces, max_ind):
    subseq = [0 for _ in range(F[max_ind])]
    i = F[max_ind] - 1
    j = max_ind
    while j != -1:
        subseq[i] = A[j]
        j = indieces[j]
        i -= 1
    
    return subseq


if __name__ == '__main__':
    print(lis([7, 4, 4, 6, 7, 8, 2, 6, 7, 8, 9, 7, 3, 1]))
