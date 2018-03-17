import numpy as np

vecx = np.array([[1, 2, 3], [4, 5, 6]])
print(vecx)
# [[1 2 3]
#  [4 5 6]]
vecy = np.array([[4, 5, 6], [7, 8, 9]])
print(vecy)
vecz = np.array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])
print(vecz)

print(vecx + vecy)
# [[ 5  7  9]
#  [11 13 15]]

print(vecx - vecy)
# [[-3 -3 -3]
#  [-3 -3 -3]]

print(np.dot(vecx, vecz))
# [[27 33 39]
#  [63 78 93]]
