"""Wiktor Wilkusz 411605
Sprawdzanie każdej możliwości rekurencją z back trackingiem.
Złożoność czasowa: O(2^n)
"""


from zad7testy import runtests

def droga( G ):
    result = []
    visited = [False for _ in range(len(G))]
    visited[0] = 1

    for v in G[0][0]:
        if (0 in G[v][0] and goto(G, v, 1, 0, result, visited)) or\
           (0 in G[v][1] and goto(G, v, 1, 1, result, visited)):
            return [0] + result

    for v in G[0][1]:
        if (0 in G[v][0] and goto(G, v, 0, 0, result, visited)) or\
           (0 in G[v][1] and goto(G, v, 0, 1, result, visited)):
            return [0] + result

    return None

def goto(G, v, destination, came_from, result, visited):
    if v == 0 and came_from == destination and all(visited):
        return True
    if visited[v]:
        return False
    
    visited[v] = True

    if came_from == 1:
        for n in G[v][0]:
            if (v in G[n][0] and goto(G, n, destination, 0, result, visited)) or\
               (v in G[n][1] and goto(G, n, destination, 1, result, visited)):
                result.append(v)
                return True
            
    elif came_from == 0:
        for n in G[v][1]:
            if (v in G[n][0] and goto(G, n, destination, 0, result, visited)) or\
               (v in G[n][1] and goto(G, n, destination, 1, result, visited)):
                result.append(v)
                return True
        
    visited[v] = False
    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
