"""
Czy spójny i policzyć spójne składowe
"""


from collections import deque


def DFS(G, visited, i):
    stack = deque()
    stack.append(i)

    visited[i] = True

    while stack:
        u = stack.pop()
        for s in G[u]:
            if not visited[s]:
                visited[s] = True
                stack.append(s)


def components(G):
    V = len(G)
    visited = [False for _ in range(V)]
    counter = 0
    
    for i in range(V):
        if not visited[i]:
            counter += 1
            DFS(G, visited, i)

    return counter


if __name__ == "__main__":
    print(components([[3, 4, 5], [4], [4, 5], [0], [0, 1, 2], [0, 2],
                      [7, 8, 9], [6, 8], [6, 7], [6]]))
