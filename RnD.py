import sys
from PySide import QtGui


class Example(object):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        print self.add(5, 6)
        print self.add_test

    def add(self, a, b):
        self.a = a
        self.b = b
        self.add_test = self.a + self.b
        return self.add_test


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()

    _add = ex.add(4, 6)
    print _add

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



#######
n, a, b = map(int, [10, 11, 12].split())
print(min(n*a, b))
