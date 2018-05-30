# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    li = sorted(A)
    li2 = []
    for i in li:
        li2.append(i)
        if li2[-1] - li2[0] > 0:
            return len(li2)

A = [6, 10, 6, 9, 7, 8]
print(solution(A))