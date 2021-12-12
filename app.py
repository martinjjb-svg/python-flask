from flask import Flask, request
from database import Database, Bookshop  # Added import of Bookshop
import json
import service
app = Flask(__name__)
db = Database()
bs = Bookshop()  # Definition for Bookshop


# GET function: Runs the hello world on local host
@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"


# GET function: Adding a sub-level to the route of the URL
@app.route("/about/")
def about():
    return "<p>About the author</p>"


# GET function: Taking in a parameter using the URL
@app.route("/square/<number>", methods=['GET'])
def square(number):
    number = int(number)  # This is required to change type to Integer
    number = number * number
    return "<p>" + str(number) + "</p>"


# Users Functionality
@app.route("/users", methods=['POST', 'GET', 'PUT'])
def users():

    # Get method
    if request.method == 'GET':
        id = request.json["id"]
        user = db.get_user_by_id(id)
        data = {"first_name": user.first_name, "last_name": user.last_name}
        return json.dumps(data)

    # POST method for
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


# Lesson 3 Books Functionality
@app.route("/books", methods=['POST', 'GET', 'PUT'])
def books():

    # Get method
    if request.method == 'GET':
        type = request.json["type"]
        info = request.json["info"]

        if type == "title":
            return service.get_book_by_title(info)  #  applies get_book_by_title method to bookshop datatbase

        if type == "author":
            return service.get_book_by_author(info)

        if type == "category":
            return service.get_book_by_category(info)

        if type == "date":
            return service.get_book_by_date(info)

        if type == "price":
            return service.get_book_by_price_lower_than(info)

    # POST method for
    if request.method == 'POST':
        title = request.json["title"]  # creates name equal to the value input next to the title key in json
        author = request.json["author"]
        category = request.json["category"]
        date = request.json["date"]
        price = request.json["price"]
        return service.add_book(title, author, category, date, price)  # adds information to bookshop database

    # PUT method for
    if request.method == 'PUT':
        id = request.json["id"]  # records the new information for each key
        title = request.json["title"]
        author = request.json["author"]
        category = request.json["category"]
        date = request.json["date"]
        price = request.json["price"]
        return service.update_book(id, title, author, category, date, price)  # applies update method


if __name__ == '__main__':
    app.run()
