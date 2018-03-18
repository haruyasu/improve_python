import math

TARGET = 2

# NUM = 1000
# list = range(NUM)
list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

low = 0
high = len(list)

while (low != high):
    center = int(math.floor((low + high) / 2))
    if (list[center] < TARGET):
        low = center + 1
    elif (TARGET < list[center]):
        high = center - 1
    else:
        break
    print("center " + str(center))
    print("low " + str(low))
    print("high " + str(high))
