"""
mamy rzeczy do wykonania i deadline

niewykonanie/wykonanie po terminie -> brak profitu
kazde zadanie zajmuje jedna godzine
trzeba znalezc maks profit

# 1 sortujemy po deadlinach, potem po profitach
    najpierw wybieramy te z najpozniejszym deadlinem
    pozostalym obnizamy deadline
    
# 2 cos jak tablica asocjacyjna
    sortujemy po profitach i wstawiamy na najpozniejsza 
    mozliwa godzine

mamy dana liste taskow i czas rozpoczecia
"""


class Task:
    def __init__(self, deadline, profit):
        self.deadline = deadline
        self.profit = profit


def find_task2(T, start):
    n = len(T)
    T.sort(key = lambda x: x.profit, reverse=True)
    maxD = 0
    for i in range(n):
        maxD = max(maxD, T[i].deadline)
    timetable = [None for _ in range(maxD - start + 1)]

    for i in range(n):
        time = T[i].deadline - start
        while time > -1 and timetable[time] is not None:
            time -= 1
        if time > -1:
            timetable[time] = T[i]
            
    return timetable
