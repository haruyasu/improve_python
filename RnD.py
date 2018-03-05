import sys
from PySide import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Check")
        self.resize(300, 100)

        panel = QtGui.QWidget()
        checkbox = QtGui.QCheckBox("Checkbox", parent=panel)
        button = QtGui.QPushButton("Push checkbox state", parent=panel)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(checkbox)
        layout.addWidget(button)
        panel.setLayout(layout)
        button.clicked.connect(checkbox.toggle)

        self.click = 100

        button.clicked.connect(self.print_state)

        print self.click

        self.setCentralWidget(panel)
        self.show()

        print self.add(5, 6)
        print self.add_test

    def print_state(self):
        self.click += 1
        print self.click


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




#
# import sys
# from PySide import QtGui
#
# def print_state(state):
#     if state:
#         print("enable")
#     else:
#         print("disable")
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     main_window = QtGui.QMainWindow()
#     main_window.setWindowTitle("Check")
#     main_window.resize(300, 100)
#     panel = QtGui.QWidget()
#     checkbox = QtGui.QCheckBox("Checkbox", parent=panel)
#     button = QtGui.QPushButton("Push checkbox state", parent=panel)
#     layout = QtGui.QVBoxLayout()
#     layout.addWidget(checkbox)
#     layout.addWidget(button)
#     panel.setLayout(layout)
#     button.clicked.connect(checkbox.toggle)
#     checkbox.stateChanged.connect(print_state)
#     main_window.setCentralWidget(panel)
#     main_window.show()
#     app.exec_()
#
# if __name__ == '__main__':
#     main()
