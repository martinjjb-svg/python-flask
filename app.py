from flask import Flask, request
from database import Database
app = Flask(__name__)
db = Database()


#GET function: Runs the hello world on local host
@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"


#GET function: Adding a sub-level to the route of the URL
@app.route("/about/")
def about():
    return "<p>About the author</p>"


#GET function: Taking in a parameter using the URL
@app.route("/square/<number>", methods=['GET'])
def square(number):
    number = int(number)  # This is required to change type to Integer
    number = number * number
    return "<p>" + str(number) + "</p>"


#Users Functionality
@app.route("/users", methods=['POST', 'GET'])
def users():

    #Get method
    if request.method == 'GET':
        user = db.get_user_by_id(0)
        data = {"first_name": user.first_name, "last_name": user.last_name}
        return data

    #POST method for
    if request.method == 'POST':
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        db.add_user(first_name, last_name)
        return "<p>new_user_added" + first_name + " " + last_name + "</p>"

if __name__ == '__main__':
    app.run()
