from flask import Flask, request
from database import Database
import json
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
@app.route("/users", methods=['POST', 'GET', 'PUT'])
def users():

    #Get method
    if request.method == 'GET':
        id = request.json["id"]
        user = db.get_user_by_id(id)
        data = {"first_name": user.first_name, "last_name": user.last_name}
        return json.dumps(data)

    #POST method for
    if request.method == 'POST':
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        user_id = db.add_user(first_name, last_name)
        response = {"id" : user_id,
                    "first_name" : first_name,
                    "last_name" : last_name}
        return json.dumps(response)

    # PUT method for
    if request.method == 'PUT':
        id = request.json["id"]
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        response = db.update_user(id, first_name, last_name)
        if response == True:
            value = {"response" : "updated"}
            return json.dumps(value)
        value = {"response": "failed"}
        return json.dumps(value)


if __name__ == '__main__':
    app.run()
