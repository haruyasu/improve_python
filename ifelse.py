for v in range(-2, 2):
    p = "foo" if v > 0 else "bar"
    print(v, p)

for v in range(-5, 5):
    p = "foo" if v > 0 else "foobar" if v < -2 else "bar"
    print(v, p)
