from peewee import *
from os import path
ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT, "activities.db"))

class Activity(Model):
    name = CharField()
    desc = CharField()
    location = CharField()
    class Meta:
        database = db

Activity.create_table(fail_silently=True)


Activity.create(name = "King Wanyama", desc = "Lecturer", location = "eMobilis")
Activity.create(name = "King Wanyams", desc = "Pastor", location = "Nairobi")
Activity.create(name = "Wanyama King", desc = "Developer", location = "eMobilis")


User1 = Activity.get(Activity.id == 1)
print(User1.name)
print(User1.desc)




