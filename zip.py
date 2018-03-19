# python2
from itertools import izip_longest
# python3
# from itertools import zip_longest

item_list = ['a', 'b', 'c', 'd']
stock_list = [1, 2, 3]

for x, y in zip(item_list, stock_list):
    print('{} / {}'.format(x, y))
# a / 1
# b / 2
# c / 3

for x, y in izip_longest(item_list, stock_list, fillvalue='nostock'):
    print('{} / {}'.format(x, y))
# a / 1
# b / 2
# c / 3
# d / nostock

#####
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
points = [100, 85, 90]
for name, age, point in zip(names, ages, points):
    print(name, age, point)
# ('Alice', 24, 100)
# ('Bob', 50, 85)
# ('Charlie', 18, 90)

#####
li = list(zip(names, ages))
print(li)
# [('Alice', 24), ('Bob', 50), ('Charlie', 18)]

#####
n = 20
s = 5
p = 4
c = 0

for a in izip_longest(*[iter(range(1, n + 1))] * s):
    c += 1
    li2 = list(a)
    # None delete
    li2 = [x for x in li2 if x is not None]
    li2 = map(str, li2)
    print(li2)
    if c == p:
        print(" ".join(li2))
# ['1', '2', '3', '4', '5']
# ['6', '7', '8', '9', '10']
# ['11', '12', '13', '14', '15']
# ['16', '17', '18', '19', '20']
