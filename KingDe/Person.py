from peewee import *
from os import path

from Activity import ROOT

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
# User.create(names="Susan Sulubu", email="kingde3@gmail.com",password="123456")
# Person.create(owner=1, names ="King", weight=85, age=27)
user1 = Person.get(Person.id == 1)
# print(user1.names)
# for person in user1.persons:
#     print(person.names, person.age, person.weight)


child = Person.get()
print(child.owner.names, child.owner.email, child.owner.password)
