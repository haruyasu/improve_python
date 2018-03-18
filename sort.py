li = [3, 5, 2, 9, 0, 4]
li.sort()
print(li)

li = sorted(li)
print(li)
# [0, 2, 3, 4, 5, 9]

#####
# reverse
li.reverse()
print(li)
# [9, 5, 4, 3, 2, 0]

#####
# key sort
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
dct = sorted(dct.items())
print(dct)
# [(0, 8), (1, 2), (2, 3), (3, 4), (4, 2)]

#####
# key sort
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items()):
    print(str(k) + ": " + str(v))
# 0: 8
# 1: 2
# 2: 3
# 3: 4
# 4: 2

#####
# key reverse
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: -x[0]):
    print(str(k) + ": " + str(v))
# 4: 2
# 3: 4
# 2: 3
# 1: 2
# 0: 8

#####
# value sort
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: x[1]):
    print(str(k) + ": " + str(v))
# 1: 2
# 4: 2
# 2: 3
# 3: 4
# 0: 8

#####
# value reverse
dct = {2: 3, 3: 4, 1: 2, 0: 8, 4: 2}
for k, v in sorted(dct.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))
# 0: 8
# 3: 4
# 2: 3
# 1: 2
# 4: 2
