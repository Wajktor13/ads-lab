def radix_sort(arr):
    n = longest_str_len(arr)
    for i in range(n - 1, -1, -1):
        counting_sort(arr, i)


def counting_sort(arr, i):
    n = len(arr)
    count = [0] * 27
    result = [0] * n

    for string in arr:
        count[index(string, i)] += 1

    for k in range(1, 27):
        count[k] += count[k - 1]

    for k in range(n - 1, -1, -1):
        result[count[index(arr[k], i)] - 1] = arr[k]
        count[index(arr[k], i)] -= 1

    for k in range(n):
        arr[k] = result[k]


def longest_str_len(arr):
    max_len = - float('inf')
    for s in arr:
        max_len = max(max_len, len(s))
    return max_len


def index(string, i):
    if len(string) <= i:
        return 0  # 0 is reserved for strings shorter than current column index
    else:
        return ord(string[i].lower()) - 96  # for ex. index of 'a' is 1


if __name__ == '__main__':
    a = ['abc', 'sdgrd', 'a', 'bc', 'fgh', 'abbbc', 'fdsd', 'ssbv',
         'ati', 'iti', 'aasf', 'abc', 'ab', 'xef', 'a', 'zze', 'ted']
    radix_sort(a)
    print(a)
