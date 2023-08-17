from copy import deepcopy


def find_min_bricks(A):
    levels_to_check, heights = get_levels_to_check_and_heights(A)
    min_bricks = float('inf')

    for level in levels_to_check:
        tmp_heights = heights.copy()
        tmp_A = deepcopy(A)
        new_tower_height = count_bricks = 0

        for i in range(len(A)):
            while tmp_heights[i] >= level:
                popped_brick = tmp_A[i].pop()
                tmp_heights[i] -= popped_brick
                new_tower_height += popped_brick
                count_bricks += 1

        while new_tower_height < level:
            highest, highest_ind = -float('inf'), None
            for i in range(len(A)):
                if tmp_A[i] != [] and tmp_A[i][-1] > highest:
                    highest, highest_ind = tmp_A[i][-1], i
            
            new_tower_height += tmp_A[highest_ind].pop()
            count_bricks += 1
        
        min_bricks = min(min_bricks, count_bricks)
    
    return min_bricks


def get_levels_to_check_and_heights(A):
    levels_to_check = []
    heights = [None for _ in range(len(A))]

    for i in range(len(A)):
        tower = A[i]
        heights[i] = sum(tower)
        tower.sort()
        level = tower[0]

        if level not in levels_to_check:
            levels_to_check.append(level)
        for brick in range(1, len(tower)):
            level = level + tower[brick]
            if level not in levels_to_check:
                levels_to_check.append(level)
    
    return levels_to_check, heights


if __name__ == "__main__":
    print(find_min_bricks([[3, 1, 3],
                           [4],
                           [2, 3],
                           [1, 1, 2, 1, 1],
                           [3, 2, 3]]))
