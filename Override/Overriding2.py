class BaseClass(object):
    def test(self):
        print("King")

class InClass(BaseClass):
    def test(self):
        print("King Wanyama")

name = InClass()
name.test()