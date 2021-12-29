import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Martin",
  password="password",
  database="test"
)

mycursor = mydb.cursor()

'''To Create database'''

#mycursor.execute("CREATE DATABASE mydatabase")

'''To Show databases'''

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
  #print(x)

'''To Create Table'''

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

'''To update Table'''

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

'''Inserting multiple records'''

#sql = "INSERT INTO books (title, author, category, date, price) VALUES (%s, %s, %s, %s, %s)"
#val = [
    #('The Alchemist', 'Coelho', 'Philosophy', '1993-01-01', '7.99'),
   # ('The Devil and Miss Prym', 'Coelho', 'Philosophy', '2002-01-01', '7'),
    #('The Shadow of the Wind', 'Zafon', 'Thriller', '2001-01-01', '7'),
    #('Hot Water', 'Wodehouse', 'Comedy', '1960-01-01', '3')
#]

#mycursor.executemany(sql, val)
#mydb.commit()
#print(mycursor.rowcount, "was inserted.")

'''Changing a record'''

#sql="UPDATE books SET author= 'King' WHERE title= 'Insidious'"
#mycursor.execute(sql)
#mydb.commit()

'''Selecting from table'''

#mycursor.execute("SELECT * FROM books")
#myresult = mycursor.fetchall()
#for x in myresult:
  #print(x)
