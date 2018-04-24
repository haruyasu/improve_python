def solution(num):
    if num < 0:
        raise ValueError

    if num == 1:
        return 1

    for i in range(int(num / 2) + 1):
        if i ** 2 == num:
            return i
        elif i ** 2 > num:
            return i - 1
    return i

print(solution(15))
# 3

# Binary Search
def better_solution(num):
    if num < 0:
        raise ValueError

    if num == 1:
        return 1

    low = 0
    high = int(num / 2) + 1

    while low + 1 < high:
        mid = low + int((high - low) / 2)
        square = mid ** 2

        if square == num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid
    return low

print(better_solution(16))
# 4