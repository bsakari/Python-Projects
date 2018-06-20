def printme( str ):
   print (str)
   return
printme("niaje")


def changeme( mylist ):
   mylist.append([1,2,3,4])
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )






def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

printme( str = "My string")



# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )





# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )