def find_sum(A, v):
    i, j = 0, len(A) - 1
    while i < j < len(A):
        s = A[i] + A[j]
        if s == v:
            return True
        elif s < v:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':

    print(find_sum([1, 2, 4, 6, 7, 11, 20, 25, 29], 33) )
    