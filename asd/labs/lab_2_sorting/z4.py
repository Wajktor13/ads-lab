"""
Write a programm that checks how many water tanks
are filled by the given amount of water.
tank - ((x1,y1),(x2,y2))
"""


def find_max_and_min_h(tanks):
    maximum = -float('inf')
    minimum = float('inf')
    for tank in tanks:
        maximum = max(maximum, tank[1][1])
        minimum = min(minimum, tank[0][1])
    return maximum, minimum


# sorting by y2 and y1 by the second instance
def quick_sort(input_list):
    def qs(a, start, end):
        left, right = start, end
        mid = a[(end + start) // 2]
        splitter = (mid[0][1], mid[1][1])  # (y1,y2)

        while left <= right:
            while a[left][0][1] < splitter[0] or (a[left][0][1] == splitter[0] and a[left][1][1] < splitter[1]):
                left += 1
            while a[right][0][1] > splitter[0] or (a[right][0][1] == splitter[0] and a[right][1][1] > splitter[1]):
                right -= 1
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        if start < right:
            qs(a, start, right)
        if end > left:
            qs(a, left, end)

    qs(input_list, 0, len(input_list) - 1)


# returns the volume of water in single tank filled to the level of water h
def volume(tank, h):
    return (tank[1][0] - tank[0][0]) * (h - tank[0][1])


# returns total volume of tanks filled to the level of water h
def total_volume(tanks, h):
    v = 0
    for tank in tanks:
        y1, y2 = tank[0][1], tank[1][1]
        if y2 <= h:
            v += volume(tank, y2)
        elif y1 < h < y2:
            v += volume(tank, h)
        else:
            break
    return v


# seeks the water level - binary search
def find_h(tanks, water):
    end, start = find_max_and_min_h(tanks)
    while True:
        h = (start + end) / 2
        used_water = total_volume(tanks, h)
        if abs(used_water - water) < 10 ** (-6):
            return round(h, 4)
        elif used_water > water:
            end = h
        elif used_water < water:
            start = h


# counts filled tanks
def filled_tanks(tanks, water):
    quick_sort(tanks)
    h = find_h(tanks, water)
    count = 0
    for tank in tanks:
        if tank[1][1] <= h:
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    t = [((10, 1), (12, 6)), ((15, 6), (17, 8)), ((2, 0), (4, 2)), ((6, 1), (8, 4))]
    print(filled_tanks(t, 24))
