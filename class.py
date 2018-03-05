class c1(object):
    def __init__(self, num):
        self.para = num

    def get_para(self):
        print self.para


class c2(object):
    def __init__(self, num):
        self.para2 = c1(num).para

    def get_para2(self):
        print self.para2

c = c1(10)
c.get_para()

c = c2(20)
c.get_para2()
