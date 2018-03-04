from PySide.QtCore import *
from PySide.QtGui import *
import sys

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        button = QPushButton('Click')
        # error
        # button.clicked.connect(self.on_click("Hello world"))
        button.clicked.connect(lambda: self.on_click("Hello world"))

        layout = QHBoxLayout()
        layout.addWidget(button)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_click(self, str):
        print(str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyForm()
    main_window.show()
    app.exec_()
