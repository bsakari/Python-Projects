# class BaseClass(object):
#     def __init__(self):
#         self.x = 10
#
# class InClass(BaseClass):
#     def __init__(self):
#         super(InClass,self).__init__()
#         self.x = 20
# number1 = InClass()
# print(number1.x)

class BaseClass(object):
    def test(self):
        print("King")


class InClass(BaseClass):
    def test(self):
        print("King Wanyama")
number1 = InClass()
number1.test()
print(BaseClass.__subclasses__())