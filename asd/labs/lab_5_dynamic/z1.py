"""
ociepka@agh.edu.pl

problem plecakowy
zachlannie - sortowanie po (wartosc / jednostka masy) malejaco i bierzemy po kolei,
jak cos sie nie miesci to bierzemy czesc
nie dziala to dla przedmiotow niepodzielnych

f(T, i, max_w) = max(f(T, i-1, max_w), f(T, i-1, max_w - W(i)) + P(i))
                 0, w <= 0
                 0, i < 0 
"""


def knapsack(W, P, max_w):
    T = [[0 for _ in range(max_w+1)] for _ in range(len(W))]
    
    for i in range(W[0], max_w+1):
        T[0][i] = P[0]

    for i in range(1, len(W)):
        for j in range(max_w+1):
            if j - W[i] < 0:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], P[i] + T[i-1][j-W[i]])

    return T[len(W) - 1][max_w]


if __name__ == "__main__":
    print(knapsack(
        [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13],
        [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312],
        850))
