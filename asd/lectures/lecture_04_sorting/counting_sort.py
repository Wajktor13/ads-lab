def counting_sort(arr, extent):
    n = len(arr)
    count = [0] * extent
    result = [None] * n
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, extent):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        result[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    for i in range(n):
        arr[i] = result[i]


if __name__ == "__main__":
    x = [7, 5, 3, 7, 9, 2, 3, 6, 2, 1, 0, 9, 4, 6]
    counting_sort(x, 10)
    print(x)