from flask import Flask, request, render_template, url_for
from database import *

app = Flask(__name__)
db = Database()

HOME = "home.html"
SIGN_UP = "sign_up.html"
MEMBERS = "see_members.html"
MEMBERSHIP = "membership.html"
LOGIN = "login.html"

@app.route('/')
def home():
    return render_template(HOME)

@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        firstname = request.form['f_name']
        lastname = request.form['l_name']
        activity = request.form['event']
        email = request.form['email']
        password = request.form['password']
        if firstname == "" or lastname == "" or activity == "" or email == "" or password == "":
            return render_template(SIGN_UP)
        else:
            db.add(firstname, lastname, email, activity, password)
        print(firstname, lastname, activity, email, password)   # for debug
    return render_template(SIGN_UP)

@app.route('/members')
def members():
    members = db.all_members()
    return render_template(MEMBERS, members=members)

@app.route('/membership', methods=["GET", "POST"])
def membership():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)  # for debug
        user_details = db.get_member(email, password)
        if user_details != None:
            print(user_details)  # for debug
            return render_template(MEMBERSHIP, user_data=user_details[0])
    return render_template(LOGIN)

@app.route('/change_name', methods=["GET", "POST"])
def change_name():
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        db.change_name(email, firstName, lastName)
        return "<h1>Changes have been made to your account</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"
    else:
        return "<h1>Wrong Method</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"

@app.route('/edit_activity', methods=["GET", "POST"])
def edit_activity():
    if request.method == 'POST':
        email = request.form['email']
        activity = request.form['event']
        db.edit_activity(email, activity)
        return "<h1>Changes have been made to your account</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"
    else:
        return "<h1>Wrong Method</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"

@app.route('/remove_member', methods=["GET", "POST"])
def remove_member():
    if request.method == 'POST':
        user_to_remove = request.form['remove_who']
        db.remove(user_to_remove)
        return "<h1>You have been removed</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"
    else:
        return "<h1>Wrong Method</h1> <br><br> <a href='/'>Home</a> <a href='members'>See memebers</a>"

if __name__ == '__main__':
    app.run()
