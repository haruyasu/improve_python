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

    def check(self, block):
        return set(block) == set(range(1, 10))


def main():
    # app = QtGui.QApplication(sys.argv)
    # ex = Example()
    #
    # _add = ex.add(4, 6)
    # print _add
    #
    # block = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print ex.check(block)
    # block = [1, 2, 3, 4, 7, 6, 7, 8, 9]
    # print ex.check(block)
    # sys.exit(app.exec_())


    # before = ["A", "E", "G", "I", "O", "S", "Z"]
    # after = ["4", "3", "6", "1", "0", "5", "2"]
    #
    # inp = "ALANTURING"
    # res = ""
    #
    # for i in inp:
    #     if i in before:
    #         num = after[before.index(i)]
    #     else:
    #         num = i
    #     res += "".join(num)
    #
    # print res

    # inp = "628381026148991X"
    # even = 0
    # odd = 0
    #
    # for i in inp:
    #
    #     if i != "X":
    #         if int(i) % 2 == 0:
    #             num = int(i) * 2
    #             plus_res = 0
    #             if num > 9:
    #                 # print "aaaa : " + str(num)
    #                 for plus in str(num):
    #                     # print plus
    #                     plus_res += int(plus)
    #                 # print plus_res
    #             else:
    #                 # print "bbbb : " + str(num)
    #                 plus_res = num
    #
    #             even += plus_res
    #             # print even
    #         else:
    #             odd += int(i)
    #             # print "kisuu = " + i
    #
    # print even
    # print odd
    #
    # res = even + odd
    # print res
    # # (x + res) % 10 == 0

    # inp = "50 40 50 60 30 80 100"
    # res = 0
    # cnt = 0
    # for i in inp.split(" "):
    #     res += int(i)
    #     cnt += 1
    #
    # a = round((float(res) / float(cnt)), 1)
    # print a

    # dic = {"1": "6", "2": "5", "3": "4", "4": "3", "5": "2", "6": "1"}
    #
    # inp = 1
    # print dic[str(inp)]

    # a = 4
    # print 6 * a**2

    # input_lines = int(input())
    # a = 0
    #
    # for i in range(input_lines):
    #     a += int(i)
    # res = 180 - a
    # print res

    # N = input()
    # a = [input() for i in range(N)]
    # print a # [a1, a2, a3, ..., aN]

    # f = open('test1.txt','r')
    # Allf = f.read()
    #
    # text = Allf.replace('\n','')
    # text = text.replace('\r','')
    # print text,
    #
    # f.close()

    # import sys
    #
    # a = []
    # for line in sys.stdin:
    #     a.append(str(line).replace('\n',''))
    #
    # print("Gold " + a[0])
    # print("Silver " + a[1])
    # print("Bronze " + a[2])

    # import sys
    # if sys.version_info[0]>=3: raw_input=input
    #
    # M=int(raw_input())
    # N=int(raw_input())
    # num=[0]*N
    # cost=[0]*N
    # total=0
    # for j in range(N):
    #     q,r=[int(e) for e in raw_input().split()]
    #     total+=q
    #     num[j]=q
    #     cost[j]=r
    # bag=[0]+[-1]*total
    # for j in range(N):
    #     for i in reversed(range(num[j],total+1)):
    #         if bag[i-num[j]]>=0:
    #             if bag[i]<0 or bag[i]>bag[i-num[j]]+cost[j]:
    #                 bag[i]=bag[i-num[j]]+cost[j]
    # j=-1
    # for i in range(M,total+1):
    #     if j<0 or (bag[i]>=0 and j>bag[i]):
    #         j=bag[i]
    # print(j)

    # import re
    #
    # text = "18k4m"
    # matchObj = re.search(r'[0-9]+', text)
    #
    # if matchObj:
    #     print matchObj.group()

    x, y = map(int, input().split())
    li = []
    for i in range(10):
        li.append(x)
        x += y

    maped_list = map(str, li)
    mojiretu = " ".join(maped_list)

    print(mojiretu)

if __name__ == '__main__':
    main()
