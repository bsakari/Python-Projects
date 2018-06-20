from peewee import *
from os import path
from Activity import ROOT
db = SqliteDatabase(path.join(ROOT, "Users.db"))

class User(Model):
    names = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db

class Person(Model):
    owner = ForeignKeyField(User, related_name="persons")
    names = CharField()
    weight = DecimalField()
    age = IntegerField()
    class Meta:
        database = db

User.create_table(fail_silently=True)
Person.create_table(fail_silently=True)
# User.create(names = "King",email = "king1@gmail.com",password = "12345")
# User.create(names = "Kingde",email = "king2@gmail.com",password = "123456")
# User.create(names = "Kingbless",email = "king3@gmail.com",password = "1234567")

Person.create(owner = 1,names = "King",weight = 85,age = 27)
Person.create(owner = 2,names = "Kingde",weight = 185,age = 270)
Person.create(owner = 3,names = "King Wanyama",weight = 285,age = 370)

User1 = User.get(User.id == 1)
print(User1.names)
print(User1.password)










