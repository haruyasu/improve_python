li = [1, 8, 14, 23, 44, 55, 67, 88, 103, 146, 150]
i = 146

low = 0
high = len(li)
center = int((low + high) / 2)

while (low <= high):
    if (i == li[center]):
        break
    elif (i > li[center]):
        low = center + 1
    elif (i < li[center]):
        high = center - 1
    center = (low + high) / 2

if (i == li[center]):
    print("Yes: " + str(center))
else:
    print("No")

#####
import bisect

li = [1, 9, 15, 32]
x = 15

print(bisect.bisect_left(li, x))
# 2

print(bisect.bisect_right(li, x))
# 3

#####
# serch
abc = "abcdefghijklmnopqrstuvwxyz"
t = "poiuytrewqlkjhgfdsamnbvcxz"
li2 = ['snn', 'xufu', 'ngebmv', 'qwtg']
n = 100

####
for k in range(n):
    li3 = []
    for i in range(len(li2)):
        res = ""
        for j in range(len(li2[i])):
            serch = (li2[i][j])
            index = (t.find(serch))
            res += (abc[index])
        li3.append(res)
    li2 = li3

print(" ".join(li2))
