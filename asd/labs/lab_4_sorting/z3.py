"""
n-char strings A, B
Over k-el alphabet
Write a program that checks if A and B are monograms
"""


# O(n + k)
def are_monograms1(a, b, k):
    # letters = [0] * k only for ints, because it copies elements
    letters = [0 for _ in range(k)]

    for i in a:
        letters[i] += 1
    
    for i in b:
        letters[i] -= 1
    
    for i in letters:
        if i != 0:
            return False
    
    return True



# O(n), we estimate that we get array arr with trash
def are_monograms2(a, b, arr):
    for letter in a:
        arr[ind(letter)] = 0
    for letter in b:
        arr[ind(letter)] = 0
    
    for letter in a:
        arr[ind(letter)] += 1
    for letter in b:
        arr[ind(letter)] -= 1
    
    for letter in a:
        if arr[ind(letter)] != 0:
            return False
    
    for letter in b:
        if arr[ind(letter)] != 0:
            return False
    
    return True

def ind(letter):
    return ord(letter) - 97
