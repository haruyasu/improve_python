class BaseClass(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


class DerivedClass(BaseClass):
    def __init__(self, a, b):
        super(DerivedClass, self).__init__(a, b)
        print self.sum()


if __name__ == "__main__":
    cls = DerivedClass(10, 20)
    print "sum : " + str(cls.sum())
    print "a : " + str(cls.a)
    print "b : " + str(cls.b)
