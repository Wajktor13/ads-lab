"""
uniwersalne ujscie - wszystkie krawedzie do niego wchodza z kazdego wierzch, zadna nie wychodzi; na macierzowej
graf niewazony, skierowany

jesli v jest uu, to dla wiersza musza byc 0, dla kolumny - 1  - 0(v^2)

da sie liniowo
jesli spotkamy 0, to ->
jesli 1 to v

jesli uu istnieje, to nigdy nie wyjdziemy dolem, zawsze prawa strona

jak wylecimy, to sprawdzamy kolumny i wiersze

"""


def is_universal_sink(G, sink):
    for v in range(len(G)):
            if sink == v:
                continue
            if not G[v][sink] or G[sink][v]:
                break
    else:
        return True

    return False


#O(V^2)
def universal_sink1(G):
    for sink in range(len(G)):
        if is_universal_sink(G, sink):
            return sink
    
    return -1


#O(V)
def universal_sink2(G):
    n = len(G)
    row = col = 0

    while row < n and col < n:
        if G[row][col] == 1:
            row += 1
        else:
            col += 1
    
    if col >= n and is_universal_sink(G, row):
        return row

    return -1 


if __name__ == "__main__":
    graph = [[0, 1, 0, 1, 1],
             [0, 0, 1, 1, 0],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 1, 0]]

    print(universal_sink1(graph))
    print(universal_sink2(graph))
