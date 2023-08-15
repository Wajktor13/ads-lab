"""
mamy dany zbior liczb
przedzial jednostkowy - obustronnie domkniety o dl. 1
ile przedzialow jednostkowych trzeba aby pokryc ten zbior

sortujemy
pierwsza liczba rozpoczyna pierwszy przedzial
szukamy pierwszej liczby, ktora nie nalezy do obecnego przedzialu

zamieniamy na podproblemy
"""


def cover(numbers):
    numbers.sort()
    counter = 0
    while numbers:
        counter += 1
        x = numbers[0]
        while numbers and numbers[0] <= x + 1:
            numbers.pop(0)
    
    return counter
