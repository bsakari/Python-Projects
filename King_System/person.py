from  peewee import *
from  os import path
ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT, "users.db"))

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

# User.create(names="John Mark", email="john@yahoo.com",password="123456")
User.create(names="Mary Jane", email="jane@yahoo.com",password="123456")
Person.create(owner=1, names ="Paul", weight=45, age=19)
Person.create(owner=1, names ="Hellen", weight=51, age=17)
Person.create(owner=2, names ="Jack", weight=61, age=21)
Person.create(owner=2, names ="Jacky", weight=56, age=25)

user1 = User.get(id=1)
print(user1.names)
# for person in user1.persons:
#     print(person.names, person.age, person.weight)


# child = Person.get(id=1)
# print(child.owner.names, child.owner.email)

#peewee relationships 1 to many







