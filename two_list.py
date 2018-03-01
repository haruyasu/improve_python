arr = [[0 for i in range(3)] for j in range(5)]
print arr

for i in range(5):
    arr[i][0] = 1
print arr

######
arr = [[]]
print arr

arr.append(0)
print arr

arr.append([1, 2, 3])
print arr

arr[0].append(5)
print arr
