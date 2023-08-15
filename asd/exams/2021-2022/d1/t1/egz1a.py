from egz1atesty import runtests

def snow( S ):
    S.sort(reverse=True)
    day = 0
    total = 0

    for area in S:
        if area - day > 0:
            total += area - day
        else:
            break
        day += 1

    return total

            
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
