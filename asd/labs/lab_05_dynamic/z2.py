"""
f(A, s, i) = f(A, s, i-1) or f(A, s-A[i], i-1)
             True, s = 0
             False, s != 0 ^ i < 0


mozna z tablica 3-wym


nonlocal i global - nie uzywac
[...] * n nie kopiuje tablic, tylko referencje
"""


def sum_subs(A, s):
    n = len(A)
    F = [[None for _ in range(n)] for _ in range(s+1)]

    return fill(A, F, s, n - 1)
    

def fill(A, F, s, i):
    if F[s][i] is not None:
        return F[s][i]
    
    F[s][i] = False

    if s == A[i]:
        F[s][i] = True

    elif i == 0:
        F[s][i] = False

    elif fill(A, F, s, i - 1):
        F[s][i] = True

    elif 0 <= s - A[i] < len(F) and fill(A, F, s - A[i], i - 1):
        F[s][i] = True
   
    return F[s][i]


if __name__ == "__main__":
    print(sum_subs([1, 2, 1, 4, 1, 3, 7, 1, 2, 5], 18))
