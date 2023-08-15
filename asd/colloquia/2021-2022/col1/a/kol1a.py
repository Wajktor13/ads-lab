from kol1atesty import runtests

def g(T):
    n = len(T)
    converted = [None] * n
    min_len, max_len = float('inf'), -float('inf')

    for i, string in enumerate(T):
        converted[i] = convert(string)
        min_len, max_len = min(min_len, len(string)), max(max_len, len(string))

    no_of_buckets = max_len - min_len + 1
    buckets = [[] for _ in range(no_of_buckets)]

    for string in converted:
        buckets[len(string) - min_len].append(string)
    
    max_strength = -float('inf')
    for b in buckets:
        if b != [] and len(b) > max_strength:
            radix_sort(b)
            strength = 1
            for i in range(1, len(b)):
                if b[i - 1] == b[i]:
                    strength += 1
                else:
                    max_strength = max(max_strength, strength)
                    strength = 1
            max_strength = max(max_strength, strength)
            strength = 1
    
    return max_strength
    

def convert(string):
    reversed = string[::-1]

    for i in range(len(string)):
        if ord(reversed[i]) < ord(string[i]):
            return reversed
        elif ord(reversed[i]) > ord(string[i]):
            return string
    
    return string


def radix_sort(A):
    strlen = len(A[0])
    for i in range(strlen):
        counting_sort(A, lambda string: ord(string[i]) - 97)


def counting_sort(A, key):
    n = len(A)
    result = [None] * n
    count = [0] * 26

    for string in A:
        count[key(string)] += 1
    
    for i in range(1, 26):
        count[i] += count[i-1]
    
    for i in range(n - 1, -1 , -1):
        result[count[key(A[i])] - 1] = A[i]
        count[key(A[i])] -= 1
    
    for i in range(n):
        A[i] = result[i]

runtests( g, all_tests=True )
