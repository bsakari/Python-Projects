try:
   textfile = open("leon.pdf", "w")
   textfile.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can't find file or read data")
else:
   print ("Written content in the file successfully")
   textfile.close()



try:
   file = open("testfile.txt", "w")
   try:
       file.write("This is my test file for exception handling!!")
   finally:
      print ("Going to close the file")
      file.close()
except IOError:
   print ("Error: can't find file or read data")






# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");



try:
    def KelvinToFahrenheit(Temperature):
        assert (Temperature >= 0), "Colder than absolute zero!"
        return ((Temperature - 273) * 1.8) + 32


    print
    KelvinToFahrenheit(273)
    print
    int(KelvinToFahrenheit(505.78))
    print
    KelvinToFahrenheit(-5)
except:
   print ("Error: can't find file or read data")
else:
   print ("Written content in the file successfully")






# User Defined Exception
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

      try:
          raise Networkerror("Bad hostname")
      except Networkerror as e:
          print (e.args)