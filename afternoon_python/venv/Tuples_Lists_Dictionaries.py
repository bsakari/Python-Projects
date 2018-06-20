# () tuple Cannot be updated
# [] list Can be updated
# {} dictionary Cannot also be updated
name1 = ("King","mimi","wewe",9,2.5,("two",7,2.5,"yes"))
# print(name1)
# print(name1[5])
# print(name1[0:4])
# print(name1[1:])

name2 = ["King","mimi","wewe",9,2.5,("two",7,2.5,"yes")]
print(name2)
# print(name2[5])
# print(name2[0:4])
# print(name2[1:])
name2[0] = "Mfalme"
print(name2)


name3 = {"King","mimi","wewe",9,2.5,("two",7,2.5,"yes")}
print(name3)
# print(name3[5])
# print(name3[0:4])
# print(name3[1:])

