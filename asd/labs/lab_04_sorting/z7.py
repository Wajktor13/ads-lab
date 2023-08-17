def shortest_range(A, k):
    n = len(A)
    min_ind, max_ind = 0, float('inf')
    colors = [0 for _ in range(k)]
    counter = 0

    i = 0
    for j in range(n):
        c = A[j]
        if colors[c] == 0:
            counter += 1
        colors[c] += 1

        if c == A[i] and colors[c] > 1:
            while colors[A[i]] > 1:
                colors[A[i]] -= 1
                i += 1
        
        if counter == k and j - i < max_ind - min_ind:
            min_ind, max_ind = i, j
    
    return min_ind, max_ind


if __name__ == '__main__':
    x = [0, 1, 4, 3, 5, 1, 2, 3, 0, 7, 1, 2, 6]
    print(shortest_range(x, 8))
