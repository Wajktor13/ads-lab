from zad3testy import runtests


def lamps( n,T ):
    colours = [0 for _ in range(n)]
    max_blue = -float('inf')

    for interval in T:
        for i in range(interval[0], interval[1] + 1):
            colours[i] += 1
        
        count_blue = 0

        for i in range(n):
            if colours[i] % 3 == 2:
                count_blue += 1
        
        max_blue = max(max_blue, count_blue)

    return max_blue

    
runtests( lamps )


