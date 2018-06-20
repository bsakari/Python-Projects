class User:
    pass
user1 = User()
user1.fname = "King"
user1.sname = "Wanyama"
print(user1.fname)
print(user1.sname)

user2 = User()
user2.fname = "Kingde"
user2.sname = "Wanyams"
print(user2.fname)
print(user2.sname)




class User:
    """This Class is accepting input from the user and give output"""
    def __init__(self,full_name,birthday):
        self.name = full_name
        self.birthday = birthday
print("Enter The Full Names and Your Birthday")
user1 = User(str(input()),str(input()))

print("Enter The Full Names and Your Birthday")
user2 = User(str(input()),str(input()))
print("Name: "+user1.name,"\nBirthday : "+user1.birthday)
print("Name: "+user2.name,"\nBirthday : "+user2.birthday)

help(User)








