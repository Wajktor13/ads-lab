counter = 0

def merge_sort(a):
    a_len = len(a)

    if a_len > 1:
        left = merge_sort(a[:(a_len // 2)])
        right = merge_sort(a[(a_len // 2):])

        return merge(left, right)

    return a


def merge(left, right):
    global counter

    result = []
    lenA, lenB = len(left), len(right)
    indA = indB = 0

    while indA < lenA and indB < lenB:
        if left[indA] <= right[indB]:
            result.append(left[indA])
            indA += 1
        else:
            counter += lenA - indA
            result.append(right[indB])
            indB += 1
    
    while indA < lenA:
        result.append(left[indA])
        indA += 1
    
    while indB < lenB:
        result.append(right[indB])
        indB += 1
    
    return result


def count_inversions(a):
    global counter
    
    merge_sort(a)

    return counter


if __name__ == '__main__':
    print(count_inversions([1, 9, 3, 6, 3, 2]))
