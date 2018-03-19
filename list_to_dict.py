li = [["a", "1"], ["b", "2"], ["c", "3"]]
d = dict(li)
print(d)
# {'a': '1', 'c': '3', 'b': '2'}

#####
keys = ["a", "b", "c"]
values = [1, 2, 3]

dic = dict(zip(keys, values))
print(dic)
# {'a': 10, 'b': 20, 'c': 30}

#####
# key merge to dict
n = 6
li2 = [[0, 200], [1, 240], [0, 120], [3, 460], [1, 240], [2, 3200]]

li2 = sorted(li2)
k = ""
li3 = []
c = 0
cnt = 0
for i in range(n):
    if k != li2[i][0]:
        li3.append([li2[i][0], li2[i][1]])
        k = li2[i][0]
        c = int(li2[i][1])
        cnt += 1
    else:
        c += int(li2[i][1])
        li3[cnt - 1][1] = c
dic = dict(li3)
print(dic)
# {0: 320, 1: 480, 2: 3200, 3: 460}
