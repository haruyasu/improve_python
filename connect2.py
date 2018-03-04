from PySide import QtGui, QtCore

class MyWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.button = QtGui.QPushButton("Click me", self)
        self.button.setCheckable(True)
        self.lineEdit = QtGui.QLineEdit(self)
        self.click = 0
        self.button.clicked.connect(self.onClicked)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.lineEdit)

    # def onClicked(self, checked):
    #     if checked:
    #         self.lineEdit.setText("Button checked")
    #     else:
    #         self.lineEdit.setText("Button unchecked")

    def onClicked(self):
        print self.sender()


        if self.click == 0:
            self.lineEdit.setText("Button checked")
            self.click += 1
        else:
            self.lineEdit.setText("Button unchecked")
            self.click -= 1

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
