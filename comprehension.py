print([i for i in range(5)])
# [0, 1, 2, 3, 4]

print({c: c.upper() for c in "abcde"})
# {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D'}

print({c for c in "abcde"})
# set(['a', 'c', 'b', 'e', 'd'])

print([i for i in range(5) if i % 2 == 0])
# [0, 2, 4]

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([j for i in values for j in i if j % 2 == 0])
# [2, 4, 6, 8]

result = [""]
n = 1
m = 2
result += [result[i % n] for i in range(n, m * n)]
print(result)
# for i in range(n, m * n):
#     result.append(result[i % n])

# lambda
prices = [10, 20, 30, 40]
li = list(map(lambda price: price * 1.08, prices))
print(li)

prices = [1, 2, 3, 4, 5, 6]
li = list(map(lambda x: x % 2, prices))
print(li)

prices = [1, 2, 3, 4, 5, 6]
li = list(filter(lambda x: x % 2 == 0, prices))
print(li)

prices = [10, 20, 30, 40, 25]
li = list(filter(lambda x: x > 20, prices))
li.sort()
print(li)