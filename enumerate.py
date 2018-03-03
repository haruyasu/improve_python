names = ["a", "b", "c", "d"]
counter = 0
for name in names:
    print(counter, name)
    counter += 1

########
# enumerate
for counter, name in enumerate(names):
    print(counter, name)

########
# zip
names = ["aa", "bb", "cc", "dd", "ee"]
numbers = [5, 2, 4, 5, 1]
print(len(names))
print(len(numbers))

for name, numbers in zip(names, numbers):
    print(name, numbers)

#######
for i, j in enumerate(range(5, 0, -1)):
    print(i, j)

for i, j in enumerate(range(5, 0, -1), start=5):
    print(i, j)
