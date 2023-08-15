from kol2btesty import runtests

"""
Process finished with exit code -1073741571 (0xC00000FD)
EXCEPTION_ACCESS_VIOLATION
"""

"""
rekurencyjnie, O(n^2) bo przegląda się tablicę do tyłu
"""

def min_cost( O, C, T, L ):
    O = [0] + O ### dodanie miasta widmo na zerowym kilometrze ###
    C = [0] + C ### i o zerowej cenie                          ###

    """
    inicjaclizacja tablicy indeksów oraz
    sortowanie indeksów po km (zamiast
    sortowania tablic O i C)
    """
    n = len(O)
    ind = [i for i in range(n)]
    ind.sort(key=lambda i:O[i]) 

    """
    inicjalizacja tablicy do spamiętywania wyników
    range(2) bo 2T wykorzystany albo nie
    """
    F = [[None for _ in range(2)]for _ in range(n)]
    F[0][0] = F[0][1] = C[ind[0]]

    """
    uruchomienie rekurencji - wypełnianie tablicy

    dwukrotne uruchomienie (used = 0, used = 1) nie
    pogarsza złożoności, dla niektórych przypadków
    bez tego może nie działać

    zaczynamy z ostatniego parkingu
    """
    mc(F, O, C, T, ind, n-1, 0)
    mc(F, O, C, T, ind, n-1, 1)


    """
    odzyskiwanie wyniku
    sprzwdzamy miasta, z których możemy 'wyjechać poza tablicę' -
    - dotrzeć do B - i bierzemy min z obliczonych cen dojazdu
    """
    min_c = float('inf')
    j = n - 1

    """
    od 0 do T wstecz
    """
    while j >= 0 and (O[ind[n-1]] + 1 - O[ind[j]]) <= T:
            if F[j][1] is not None: min_c = min(min_c, F[j][1])
            j -= 1

    """
    od T+1 do 2T wstecz
    """
    while j >= 0 and (O[ind[n-1]] + 1 - O[ind[j]]) <= 2 * T:
        if F[j][1] is not None: min_c = min(min_c, F[j][0])
        j -= 1


    return min_c


"""
parametry:F - tablica do spamiętywania
          O, C, T - jw
          ind - tablica indeksów
          i - indeks obecnie rozważanego parkingu
          u - 'used' - czy 2T wykorzystany
"""
def mc(F, O, C, T, ind, i, u):
    """
    mamy zapisany wynik, zwracamy go
    """
    if F[i][u] is not None:
        return F[i][u]

    
    """
    nie mamy wyniku, ustalamy na inf i szukamy min
    kosztu dojazdu + postoju na danym parkingu
    """
    F[i][u] = float('inf')
    n = len(O)

    """
    do T wstecz, 2T niewykorzystany
    """
    j = i - 1
    if not u:
        while j >= 0 and (O[ind[i]] - O[ind[j]]) <= T:
                F[i][u] = min(F[i][u], mc(F, O, C, T, ind, j, 0) + C[ind[i]])
                j -= 1                                 ###^^^ - zmiana (i-1) na j ### 
                                                        
    """
    do T i wykorzystany, lub do 2T i wykorzystujemy
    czyli chcemy, żeby 2T było wykorzystane
    """ 
    j = i - 1
    if u:
        """
        2T wykonany wczesniej
        """
        while j >= 0 and (O[ind[i]] - O[ind[j]]) <= T:
            F[i][u] = min(F[i][u], mc(F, O, C, T, ind, j, 1) + C[ind[i]])
            j -= 1                                 ###^^^ - zmiana (i-1) na j ###
        
        """
        wykonujemy 2T
        j zostawiamy z tego wyżej
        """
        while j >= 0 and (O[ind[i]] - O[ind[j]]) <= 2 * T:
            F[i][u] = min(F[i][u], mc(F, O, C, T, ind, j, 0) + C[ind[i]])
            j -= 1                                 ###^^^ - zmiana (i-1) na j ###
    
    return F[i][u]


runtests( min_cost, all_tests = True )
