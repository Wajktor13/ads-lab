def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = transform(T[i])

    counting_sort_by_key(T, lambda a: a[2])
    counting_sort_by_key(T, lambda a: a[1])

    j = n - 1
    for i in range(n // 2):  # reversing and retransforming
        T[i], T[j] = T[j][0], T[i][0]
        j -= 1


def transform(num):
    n = num
    digits = [0] * 10
    while n > 0:
        digits[n % 10] += 1
        n //= 10

    single = multi = 0
    for counter in digits:
        if counter == 1:
            single += 1
        elif counter > 1:
            multi += 1

    return num, single, multi


def counting_sort_by_key(arr, key):
    n = len(arr)
    counter = [0] * 10

    for data in arr:
        counter[key(data)] += 1

    for i in range(1, 10):
        counter[i] += counter[i-1]

    result = [None] * n
    for i in range(n):
        result[counter[key(arr[i])] - 1] = arr[i]
        counter[key(arr[i])] -= 1

    for i in range(n):
        arr[i] = result[i]


if __name__ == '__main__':
    x = [1266, 114577, 2344, 67333, 4432, 653, 8811, 2]
    pretty_sort(x)
    print(x)
