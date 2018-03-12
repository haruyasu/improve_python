li = ["a1", "b2", "c3"]
res = ""
for i in li:
    res += i
print(res)

###########
res = " ".join(li)
print(res)

###########
res = ",".join(li)
print(res)

###########
li = [1, 2, 3]
str_li = map(str, li)
res = " ".join(str_li)
print(res)

###########
s = "a1 a2 a3"
str_list = []
temp = ""

for i in s:
    if(i == " "):
        str_list.append(temp)
        temp = ""
    else:
        temp += i

if(temp != ""):
    str_list.append(temp)
print(str_list)

###########
str_list = s.split()
print(str_list)

###########
class Test():
    def __init__(self):
        self.testList = []

    def main(self):
        self.testList.append("abc")
        self.testList.append("def")
        self.testStr = " ".join(self.testList)
        print self.testStr

if __name__ == '__main__':
    test = Test()
    test.main()

###########
