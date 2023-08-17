def select(T):  # task - (starting time, ending time)
    T.sort(key=lambda task: task[1])
    result = [T[0]]
    for task in T:
        if not task[0] < result[-1][1]:
            result.append(task)
    return result


if __name__ == '__main__':
    print(select([(5.5, 7.5), (9, 12), (7, 12), (2, 3), (1.5, 3.5), (1, 4), (10, 11), (0, 2),
                  (3, 6), (5, 8), (1, 4), (9.5, 11.5), (1, 6), (8, 13), (7, 10), (11, 14)]))
