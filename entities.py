class User:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {"id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name
                }


class Book:

    def __init__(self, id, title, author, category, date, price):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.date = date
        self.price = price

    #  Method sets out the new record of information to add to new list "low"
    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "author": self.author,
                "category": self.category,
                "date": self.date,
                "price": self.price
                }
