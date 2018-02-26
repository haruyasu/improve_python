print [i for i in range(5)]

print {c: c.upper() for c in "abcde"}

print {c for c in "abcde"}

print (c.upper() for c in "abcde")

print [i for i in range(5) if i % 2 == 0]

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [j for i in values for j in i if j % 2 == 0]
