"""
Czy w G istnieje cykl dl 4?

1 - brute force - bierzemy każde 4 i spr czy da się stworzyć z nich cykl - O(V^4)
2 - dfs na głębokość 4
3 - dla każdych 2 wierzchołków sprawdzamy, czy mają 2 wspólnych sąsiadów - O(V^3)
"""

def has_4cycle(G):
    V = len(G)
    for a in range(V):
        for b in range(a + 1, V):
            counter = 0
            for c in range(V):
                if G[a][c] and G[b][c]: #reprezentacja macierzowa
                    counter += 1
                    if counter >= 2:
                        return True
    return False


if __name__ == "__main__":
    print(has_4cycle([[0, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0],
                      [0, 1, 0, 1, 1, 0],
                      [0, 0, 1, 0, 0, 1],
                      [1, 0, 0, 1, 1, 0]]))
