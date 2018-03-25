h = 7
w = 10
n = 1
# li = [[1, 8, 1], [4, 1, 5], [1, 6, 2], [2, 2, 0]]
li = [[2, 0, 2]]

####
li2 = []
for i in range(h):
    li_ = []
    for j in range(w):
        li_.append(".")
    li2.append(li_)

for i in range(n):
    h1 = li[i][0]
    w1 = li[i][1]
    x1 = li[i][2]

    li3 = []
    for j in range(h):
        for k in range(w):
            if li2[j][k] == "#":
                li3.append([j, k])
    print(li3)

    for j in range(h):
        for k in range(w):
            if 0 <= k <= 1:
                if j == 6 or j == 5:
                    li2[j][k] = "#"
            # if x1 <= k < (w1 + x1):
            #     if j == h - 1:
            #         li2[j][k] = "#"


for i in range(h):
    print(li2[i])
