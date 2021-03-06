import argparse
import sys
from PySide.QtCore import *
from PySide.QtGui import *

BOARDS = ["debug", "n00b", "l33t", "error"]
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--board", help="Desired board name", type=str, choices=BOARDS, required=True)
    args = vars(arg_parser.parse_args())
    return args["board"]


class GUI(QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.start_puzzle = [[2, 1, 0, 0, 0, 0, 4, 0, 0],
                             [3, 8, 0, 4, 0, 0, 7, 0, 2],
                             [0, 0, 0, 7, 2, 0, 0, 0, 0],
                             [0, 2, 4, 8, 0, 6, 9, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 1, 2, 0, 3, 5, 4, 0],
                             [0, 0, 0, 0, 5, 8, 0, 0, 0],
                             [9, 0, 3, 0, 0, 4, 0, 2, 8],
                             [0, 0, 8, 0, 0, 0, 0, 5, 7]]

        self._initUI()

    def _initUI(self):
        self.setWindowTitle("Sudoku")
        self.resize(500, 500)

        self.puzzle = []

        for i in xrange(9):
            self.puzzle.append([])
            for j in xrange(9):
                self.puzzle[i].append(self.start_puzzle[i][j])

        for i in xrange(9):
            for j in xrange(9):
                self.answer = self.puzzle[i][j]
                x = MARGIN + j * SIDE + SIDE / 2
                y = MARGIN + i * SIDE + SIDE / 2
                original = self.start_puzzle[i][j]
                color = "black" if self.answer == original else "sea green"

                if self.answer != 0:
                    self.number = QLabel(str(self.answer), self)
                else:
                    self.number = QLabel("", self)

                self.number.move(x, y)
                self.number.mouseDoubleClickEvent = self._clickedText

    def _clickedText(self, event):
        self.number.setText = self.answer
        print self.answer


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        for i in xrange(10):
            if i % 3 == 0:
                pen = QPen(Qt.blue, 1, Qt.SolidLine)
                qp.setPen(pen)
            else:
                pen = QPen(Qt.gray, 1, Qt.SolidLine)
                qp.setPen(pen)

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            qp.drawLine(x0, y0, x1, y1)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            qp.drawLine(x0, y0, x1, y1)


        # layout = QVBoxLayout()
        # self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # board_name = parse_arguments()
    # print board_name
    #
    # with open("%s.sudoku" % board_name, "r") as board_file:
    #     game = SudokuGame(board_file)

    main()
