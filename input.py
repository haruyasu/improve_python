# python2
# row_input()

# python3
# input()

# IN abcde
s = input()
# OUT "abcde"

# IN abcde
s = list(input())
# OUT ["a", "b", "c", "d", "e"]

# IN 5
a = int(input())
# OUT 5

# IN 1 2
x, y = map(int, input().split())
# OUT x = 1, y = 2

# IN 1 2 3 4 ... n
li = input().split()
# OUT ["1", "2", "3"...."n"]

# IN 1 2 3 4 ... n
li = list(map(int, input().split()))
# OUT [1, 2, 3, 4 ... n]

# IN 1,2,3,4....n
li = list(map(int, input().split(",")))
# OUT [1, 2, 3, 4 ... n]

###################
# IN
# 3
# test1
# test2
# test3
n = int(input())
s = [input() for i in range(n)]
# OUT ["test1", "test2", "test3"]

# IN
# a1
# a2
# a3
# ...
# -1 <- finish
a = []
while True:
    n = input()
    if n == -1:
        break
    a.append(n)
print a
# OUT ["a1", "a2", "a3"]

# IN
# 1
# 2
# 3
# ...
# (EOF)
import sys

a = []
for line in sys.stdin:
    a.append(int(line))
print a
# OUT [1, 2, 3]

# IN
# a
# b
# c
# ...
# (EOF)
import sys

a = []
for line in sys.stdin:
    a.append(str(line).replace('\n', ''))
print a
# OUT ["a", "b", "c"]

# IN
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2
li = []
while True:
    try:
        li.append(list(map(int, input().split())))
    except:
        break
print li
# OUT [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

# IN
# 3
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2
n = int(input())
li = []
li.append(list(map(int, input().split())) for i in range(n))
print li
# OUT [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]

###############
# a = -1, b = -2
print(a / b)
# 0.5

print("%lf" % (a / b))
# 0.500000

print("%1f" % (a / b))
# 0.5

print(str(a / b))
# "0.5"

##############
import bisect

li = [1,2,5,2,4,6,7,8,6,56,3,56,76,34,32,2,6,0,32,6,0]
index = bisect.bisect_right(sorted(li), 0)
clearli = li[index:]
print clearli
