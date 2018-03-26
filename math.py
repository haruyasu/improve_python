oy = 10
s = 15
c = 45
x = 10
y = 10
a = 10
####
import math

g = 9.8

rad = math.radians(c)
yy = oy + x * math.tan(rad) - ((g * (x ** 2)) / (2 * (s ** 2) * (math.cos(rad) ** 2)))
h = y - yy
h = round(h, 1)
if abs(h) <= a / 2:
    print("Hit " + str(h))
else:
    print("Miss")
