"""
Write an algorithm that finds the leader* of the sequence.
Assume, that the leader exists.
Required time complexity: O(n)

leader - number that appears in more than half of the array.
"""


def find_leader(arr):
    leader = None
    count = 0
    for num in arr:
        if num != leader and count == 0:
            leader = num
            count = 1
        elif num != leader:
            count -= 1
        else:
            count += 1
    return leader


if __name__ == '__main__':
    print(find_leader([1, 1, 4, 1, 1, 2, 1, 1, 3, 5, 5, 5, 1, 1, 5]))
