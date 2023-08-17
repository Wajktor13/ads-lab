def merge_sort(A):
    n = len(A)
    end = False

    while not end:
        i = j = k = 0
        while i < n:
            while j < n - 1 and A[j] <= A[j + 1]:
                j += 1
            
            if i == 0 and j == n - 1:
                end = True
                break

            k = j + 1
            while k < n - 1 and A[k] <= A[k + 1]:
                k += 1
            
            A = A[:i] + merge(A[i:j+1], A[j+1:k+1]) + A[k+1:]
            
            i = j = k + 1
    
    return A


def merge(A, B):
    result = []
    lenA, lenB = len(A), len(B)
    indA = indB = 0

    while indA < lenA and indB < lenB:
        if A[indA] <= B[indB]:
            result.append(A[indA])
            indA += 1
        else:
            result.append(B[indB])
            indB += 1
    
    while indA < lenA:
        result.append(A[indA])
        indA += 1
    
    while indB < lenB:
        result.append(B[indB])
        indB += 1
    
    return result


if __name__ == '__main__':
    print(merge_sort([1, 7, 3, 4, 5, 6, 8, 9, 2, 3, 54, 2, 1]))
