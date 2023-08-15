from kol1btesty import runtests

def f(T):
    n = len(T)
    signatures = [convert(T[i]) for i in range(n)]
    radix_sort(signatures)

    max_popularity = 0
    current_popularity = 1
    for i in range(1, n):
        if signatures[i - 1] == signatures[i]:
            current_popularity += 1
        else:
            max_popularity = max(max_popularity, current_popularity)
            current_popularity = 1
    max_popularity = max(max_popularity, current_popularity)
    current_popularity = 1
 
    return max_popularity


def convert(string):
    signature = [0 for _ in range(26)]

    for letter in string:
        signature[ord(letter) - 97] += 1
    
    return signature


def radix_sort(T):
    for i in range(26):
        counting_sort(T, lambda signature: signature[i])


def counting_sort(T, key):
    n = len(T)

    min_val, max_val = float('inf'), -float('inf')
    for signature in T:
        min_val, max_val = min(min_val, key(signature)), max(max_val, key(signature))
    r = max_val - min_val + 1

    count = [0 for _ in range(r)]
    result = [None for _ in range(n)]

    for element in T:
        count[key(element) - min_val] += 1
    
    for i in range(1, r):
        count[i] += count[i - 1]

    for i in range(n - 1, -1 , -1):
        result[count[key(T[i]) - min_val] - 1] = T[i]
        count[key(T[i]) - min_val] -= 1
    
    for i in range(n):
        T[i] = result[i]
    

runtests( f, all_tests=True )
