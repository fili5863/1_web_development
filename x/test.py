import sqlite3


# Connect to the db
db = sqlite3.connect("company.db")

# Runs the command in the db
q = db.execute("SELECT * FROM users")

# Parses data from db to python
users = q.fetchall()

# Prints the data in terminal
print(users)

