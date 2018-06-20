from flask import Flask,render_template,request,flash
from  users_models import User
app = Flask(__name__)
app.secret_key="super_secret_key"

@app.route('/')
def hello_world():
    users = User.select()
    return render_template("home.html",users=users)

@app.route('/add',methods=("GET","POST"))
def add():
     if request.method=="POST":
         names =request.form["names"]
         email= request.form["email"]
         age =request.form["age"]
         User.create(names=names, email=email, age=age)
         flash("User Saved")
     return render_template("add.html")

if __name__ == '__main__':
    app.run()
