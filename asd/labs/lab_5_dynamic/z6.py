"""
nominaly 
musimy wydac konkretna kwote, mamy nogr monety
uzywamy jak najmniejszej liczby monet

(mozna zachlannie, bo kazdy nominal jest min 2*wiekszy i mamy jednostkowy (Zwsze bierzemy najw) <- dla pln, 
dla innych nominalow to nie musi dzialac)


ile monet minimalnie - dla dowolnych nominalow
zakladamy ze da sie wydac zadana kwote

N - zbior nominalow
f(k, N) = 1, k e N
          inf, v : k < n
             n e N
          min ({f(k-n, N) | k >= n}) + 1
         n e N

"""


def min_coins(coins, amount):
    coins.sort()

    f = [float('inf') for _ in range(amount + 1)]
    f[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a < c:
                break
            f[a] = min(f[a], f[a - c] + 1)

    return f[amount]


if __name__ == "__main__":
    print(min_coins([50, 20, 2, 1, 3, 11], 84))
