# User Defined Exception
class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.argsv = arg

        try:
            raise Networkerror("Bad hostname")
        except Networkerror as e:
            print(e.args)

try:
    def tempconvert(Temperature):
        assert (Temperature >= 0), "Colder Than Absolute Zero"
        return ((Temperature - 273)*1.8) + 32
    print(tempconvert(273))
    print(int(tempconvert(505.78)))
    print(tempconvert(-5))
except:
    print("Error")
else:
    print("success")












