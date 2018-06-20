#() Tuple. Can't be updated
#[] List. Can be updated
#{} Dictionary. Can't be updated

#Tuple
name1 = ("King","Wanyama","Hello","World")
print(name1)
print(name1[0])
print(name1[0:3])
print(name1[1:])
#List
name2 = ["King","Wanyama","Hello","World"]
print(name2)
print(name2[0])
print(name2[0:3])
print(name2[1:])
name2[3] = "King"
print(name2)
#Dictionary
name3 = {"King","Wanyama","Hello","World"}
print(name3)

