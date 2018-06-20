# import peewee
from  peewee import *
import datetime

db = MySQLDatabase("cheki", host="localhost", user="root", passwd="")


class Car(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()
    number_plate = CharField()

    class Meta:
        database = db
        db_table = "cars"
class Buyer(Model):
    names =CharField()
    email = CharField(unique=True)
    tarehe =DateField(default=datetime.datetime.today())

    class Meta:
        database = db
        db_table = "buyers"


