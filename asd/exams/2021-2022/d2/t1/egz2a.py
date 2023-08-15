"""Wiktor Wilkusz 411605

Algorytm wykorzystuje drzewo przedziałowe, w którym przedział (first_ind, last_ind) reprezentuje
magazyny od first_ind do last_ind. W węzłach, oprócz standardowych połączeneń między innymi węzłami
oraz oznaczeń danego przedziału, występuje zmienna max_remaining, która przechowuje maksymalną
pojemność dostępną w danym poddrzewie. Budowa drzewa polega na sklejaniu węzłów do par. Z każdą
iteracją rozmiar danych zmniejsza się dwukrotnie, więc złożoność czasowa wynosi O(nlogn)

Algorytm:
Dla każdego kolejnego transportu wyszukujemy najlepszy węzeł. Podczas jego wyszukiwania  zawsze,
jeśli możemy (istnieje lewe dziecko i pojemność jest wystarczająca), idziemy w lewo - w celu
znalezienie minimalnego indeksu. Znaleziony węzeł zostaje zaktualizowany (zmniejsza się jego
pozostałą pojemność o aktualnie rozpatrywaną wagę), a następnie aktualizowani są rodzice w górę drzewa.

Złożoność: O(nlogn)
"""


from egz2atesty import runtests


# węzeł drzewa przedziałowego
class TreeNode:
    def __init__(self, first_ind, last_ind, initial_capacity):
        self.first_ind = first_ind
        self.last_ind = last_ind
        self.max_remaining = initial_capacity
        self.left_child = None
        self.right_child = None
        self.parent = None
    

def coal( A, T ):
    n = len(A)

    # inicjalizacja węzłów
    nodes = [TreeNode(i, i, T) for i in range(n)]
    
    # budowa drzewa przedziałowego
    m = len(nodes)
    while m > 1:
        tmp = []
        for i in range(0, m - 1, 2):
            n1, n2 = nodes[i], nodes[i + 1]
            new_node = TreeNode(n1.first_ind, n2.last_ind, T)
            new_node.left_child, new_node.right_child = n1, n2
            n1.parent = n2.parent = new_node
            tmp.append(new_node)

        if m % 2 != 0:
            tmp.append(nodes[-1])

        nodes = tmp
        m = len(nodes)
    
    # umieszczanie transportów w magazynach
    root = nodes[0]
    last_ind = 0
    for weight in A:
        node = root

        # wyszukiwanie najlepszego węzła - liścia
        while node.left_child is not None and node.right_child is not None:
            if node.left_child is not None and node.left_child.max_remaining >= weight:
                node = node.left_child
            elif node.right_child is not None and node.right_child.max_remaining >= weight:
                node = node.right_child
        
        last_ind = node.first_ind

        # aktualizacja znalezionego węzła
        node.max_remaining = node.max_remaining - weight

        # aktualizacja rodziców
        while node is not None:
            if node.left_child is not None and node.right_child is not None:
                if node.left_child.max_remaining >= node.right_child.max_remaining:
                    node.max_remaining = node.left_child.max_remaining
                else:
                    node.max_remaining = node.right_child.max_remaining
            elif node.left_child is not None:
                node.max_remaining = node.left_child.max_remaining
            elif node.right_child is not None:
                node.max_remaining = node.right_child.max_remaining
            
            node = node.parent
    
    return last_ind


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
