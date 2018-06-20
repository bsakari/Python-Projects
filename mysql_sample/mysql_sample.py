from flask import Flask
from models import Car, Buyer
from  peewee import IntegrityError
app = Flask(__name__)


@app.route('/')
def add():
 # Car.create(make="Mercedes",model="C Class",year=2017,number_plate="KCK 200A")
 # for car in Car.raw("select * from cars"):
 #     print(car.year)
 b1 =Buyer.select().execute()
 print(type(b1))

 # try:
 #    Buyer.create(names="John Terry", email="terry@chelsea.com")
 # except IntegrityError:
 #     print("User already exists")
 return 'Created!'


if __name__ == '__main__':
    app.run()
