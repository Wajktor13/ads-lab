"""Wiktor Wilkusz 411605
Algorytm zachłanny. W każdym kroku wykonuje maksymalny ruch do przodu,
a następnie uzupełnia paliwo z największej z napotkanych plam ropy, które
to są zapisywane w kolejce priorytetowej. Priorytetem jest objętość danej
plamy pomnożona przez -1 (aby odwrócić kolejkę), a przechowywaną
informacją - indeks tej plamy.

Uzasadnienie poprawności: jeśli brakuje nam paliwa na dojechanie do pola
n-1 (czyli musimy się gdzieś zatrzymać) to wybieramy pole z lewej strony,
z którego zatankujemy najwięcej, co zminimalizuje potrzebną liczbę
przystanków w dalszej części podróży.

Złożoność obliczeniowa: O(nlog(n))
"""


from zad5testy import runtests
import queue


def plan(T):
    n = len(T)
    pq = queue.PriorityQueue(maxsize=n - 2)
    i = 0
    fuel = T[0]
    result = [0]

    while i + fuel < n - 1:

        for j in range(i + 1, i + fuel + 1):
            if T[j] > 0:
                pq.put(((-1) * T[j], j))

        i += fuel
        largest_stain = pq.get()
        result.append(largest_stain[1])
        fuel = (-1) * largest_stain[0]

    return sorted(result)


runtests(plan, all_tests=True)
