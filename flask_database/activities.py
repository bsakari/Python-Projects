from  peewee import *
from  os import path
ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT, "activities.db"))

class Activity(Model):
    name = CharField()
    desc = CharField()
    location = CharField()
    class Meta:
        database = db
Activity.create_table(fail_silently=True)
Activity.create(name="Water Day", desc="Celebrating Water Diving",location="Nanyuki")
Activity.create(name="Running", desc="Eldoret Marathon",location="Eldoret")