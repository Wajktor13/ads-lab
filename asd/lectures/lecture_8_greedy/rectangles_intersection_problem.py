def rect_intersection1(A):  # rect - ((x1, y1), (x2, y2))
    n = len(A)
    max_area, to_remove = -float('inf'), None

    for candidate_for_removal in range(n):
        left = right = top = bottom = candidate_for_removal + 1 if candidate_for_removal < n - 1 else candidate_for_removal - 1
        for i in range(n):
            if i != candidate_for_removal:
                left, right, top, bottom = find_edges(A, i, left, right, top, bottom)
        
        side, base = (A[right][1][0] - A[left][0][0]), (A[top][0][1] - A[bottom][1][1])
        area = side * base
        
        if area > max_area and side > 0 and base > 0:
            max_area, to_remove = area, A[candidate_for_removal]
    
    return max_area, to_remove


def rect_intersection2(A):
    n = len(A)
    L, R = [0] * n, [0] * n
    L[0] = R[-1] = ((-float('inf'), float('inf')),
                    (float('inf'), -float('inf')))

    for i in range(n - 1):
        L[i + 1] = find_coords(A[i], L[i])
        R[-i - 2] = find_coords(A[-i - 1], R[-i - 1])

    max_area, to_remove = -float('inf'), None
    for i in range(n):
        rect = find_coords(L[i], R[i])
        side, base = (rect[1][0] - rect[0][0]), (rect[0][1] - rect[1][1])
        area = side * base
        if area > max_area and side > 0 and base > 0:
            max_area = area
            to_remove = i

    return max_area, A[to_remove]


def rect_intersection3(A):
    n = len(A)
    to_check = []

    left = right = top = bottom = 0
    for i in range(1, n):
        left, right, top, bottom = find_edges(A, i, left, right, top, bottom)

    if unique_edge(A, left, 0, 0):
        to_check.append(left)
    if unique_edge(A, right, 1, 0) and right not in to_check:
        to_check.append(right)
    if unique_edge(A, top, 1, 1) and top not in to_check:
        to_check.append(top)
    if unique_edge(A, bottom, 0, 1) and bottom not in to_check:
        to_check.append(bottom)

    max_area = -float('inf')
    to_remove = None
    for rect in to_check:
        left = right = top = bottom = rect - 1 if rect > 0 else rect + 1
        for i in range(n):
            if i == rect:
                continue
            left, right, top, bottom = find_edges(
                A, i, left, right, top, bottom)

        side, base = (A[right][1][0] - A[left][0][0]), (A[top][0][1] - A[bottom][1][1])
        area = side * base

        if area > max_area and side > 0 and base > 0:
            max_area = area
            to_remove = rect

    return max_area, A[to_remove]


def find_coords(rect1, rect2):
    x1 = max(rect1[0][0], rect2[0][0])
    x2 = min(rect1[1][0], rect2[1][0])
    y1 = min(rect1[0][1], rect2[0][1])
    y2 = max(rect1[1][1], rect2[1][1])
    return ((x1, y1), (x2, y2))


def unique_edge(A, ind, i, j):
    value = A[ind][i][j]
    n = len(A)
    for k in range(n):
        if k == ind:
            continue
        if A[k][i][j] == value:
            return False
    return True


def find_edges(A, i, left, right, top, bottom):
    if A[i][0][0] > A[left][0][0]:
        left = i
    if A[i][1][0] < A[right][1][0]:
        right = i
    if A[i][0][1] < A[top][0][1]:
        top = i
    if A[i][1][1] > A[bottom][1][1]:
        bottom = i

    return left, right, top, bottom


if __name__ == '__main__':
    arr1 = [((5, 7), (11, 4)), ((1, 6), (7, 1)), ((4, 10), (10, 3)), ((3, 14), (13, 2)),
           ((0, 5), (15, 0)), ((250, 200), (300, 250))]
    
    arr2 = [((5, 7), (11, 4)), ((1, 6), (7, 1)), ((4, 10), (10, 3)), ((3, 14), (13, 2)),
           ((0, 5), (15, 0))]

    print(rect_intersection1(arr1), rect_intersection2(arr1), rect_intersection3(arr1))

    print(rect_intersection1(arr2), rect_intersection2(arr2), rect_intersection3(arr2))
