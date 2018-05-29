# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # write your code in Python 3.6

    if len(S) % K == 0:
        return int(len(S) / K)
    else:
        return int(len(S) / K) + 1

S = "SMS messages are really short"
K = 16
print(solution(S, K))
