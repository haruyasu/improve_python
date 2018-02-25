# normal
class Sample:
    def __init__(self):
        self.text = "Sample"

    def get_text(self):
        return "({0})".format(self.text)

    def set_text(self, text):
        if text is None:
            self.text = ""
        else:
            self.text = text

    def delete_text(self):
        pass


obj = Sample()
print(obj.get_text())
obj.set_text(None)
obj.delete_text()


###########
# @property
class Sample2:
    def __init__(self):
        self.__text = "Sample"

    @property
    def text(self):
        return "({0})".format(self.__text)

    @text.setter
    def text(self, text):
        if text is None:
            self.__text = "None"
        else:
            self.__text = text

    @text.deleter
    def text(self):
        pass


obj2 = Sample2()
print(obj2.text)

obj2.text = None
print(obj2.text)

del obj2.text
print(obj2.text)
