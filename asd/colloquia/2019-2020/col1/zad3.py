import random


def check(T):
    n = len(T)
    T.sort()
    
    for i in range(n):
        value = T[i]
        left, right = 0, n-1
        found = False

        while left < right:
            if left == i:
                    left += 1
            if right == i:
                    right -= 1

            total = T[left] + T[right]
            if total == value:
                found = True
                break
            elif total < value:
                left += 1
            else:
                right -= 1
                

        if not found:
            return False
    
    return True


if __name__ == '__main__':
    while True:
        arr = [-5, -2, -5, 0, 0, 0, -2, 7, 4, 7, 4]
        for k in range(5000):
            length = len(arr)
            i, j = random.randint(0, length -3), random.randint(0, length -3)
            if i == j:
                i += 1
            arr.append(arr[i] + arr[j])

        if not check(arr):
            break

        print('ok')
