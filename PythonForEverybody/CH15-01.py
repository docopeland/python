# Instructions
# Create a SQLITE database or use an existing database and create a table in the database called "Ages":
# CREATE TABLE Ages (
#   name VARCHAR(128),
#   age INTEGER
# )
# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only
# these rows with the following commands:
#
# DELETE FROM Ages;
# Insert rows: ('Gabby', 27); ('Benn', 39); ('Abdulkhader', 37); ('Esther', 30); ('Jaii', 39); ('Romi', 24);
# Once the inserts are done, run the following SQL command:
# SELECT hex(name || age) AS X FROM Ages ORDER BY X
#
# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
# Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other
# database. So you cannot use MySQL or Oracle for this assignment.

import sqlite3

# connect and get a cursor for sqlite
conn = sqlite3.connect("sql1.db")
curr = conn.cursor()

# deleting table ages if it exists, if it doesn't nothing happens
curr.execute("DROP TABLE IF EXISTS Ages")
# creating new ages table
curr.execute("CREATE TABLE Ages(name TEXT, age INTEGERS)")

# insert values into the table and commit
curr.execute("INSERT INTO Ages (name, age) VALUES ('Gabby', 27)")
curr.execute("INSERT INTO Ages (name, age) VALUES('Benn', 39)")
curr.execute("INSERT INTO Ages (name, age) VALUES ('Abdulkhader', 37)")
curr.execute("INSERT INTO Ages (name, age) VALUES ('Esther', 30)")
curr.execute("INSERT INTO Ages (name, age) VALUES ('Jaii', 39)")
curr.execute("INSERT INTO Ages (name, age) VALUES ('Romi', 24)")
conn.commit()

SQLcommand = curr.execute("SELECT hex(name||age) AS X FROM Ages ORDER BY X")
row = [rows[0] for rows in SQLcommand]
print(row[0])