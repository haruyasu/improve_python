lis = []
lis.append(1)
lis.append(2)
lis.append(3)
print lis

lis2 = []
lis2 += [11, 22, 33]
print lis2

lis3 = []
lis3.extend([111, 222, 333])
print lis3

######
# sort doble list
li2 = [[3, 5, 9], [15, 20, 35], [30, 45, 72], [15, 20, 31], [27, 33, 59], [27, 35, 77]]
li3 = sorted(li2, reverse=True)
for i in li3:
    print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]))
