# Instructions
# This application will read roster data in JSON format, parse the file, and then produce an SQLite database that
# contains a User, Course, and Member table and populate the tables from the data file.
#
# Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data,
# run the following SQL command:
#
# SELECT User.name,Course.title, Member.role FROM
#     User JOIN Member JOIN Course
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
# The output should look as follows:
# Zoha|si430|0
# Ziyaan|si334|0
# Once that query gives the correct data, run this query:
# SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
#     User JOIN Member JOIN Course
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY X LIMIT 1;
# You should get one row with a string that looks like XYZZY53656C696E613333.

import json
import sqlite3

# open the file
file = input("Enter file: ")
if len(file) <1: file = "files/roster_data.json"
fOpen = open(file).read()

# set up sql connection & cursor
conn = sqlite3.connect("roster.sqlite")
curr = conn.cursor()

# drop & create the sql tables
curr.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE);
CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE);
CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER);""")

# load the data
js = json.loads(fOpen)
for entry in js:
    name = entry[0]
    course = entry[1]
    role = entry[2]
    # get user_id
    curr.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name,))
    curr.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = curr.fetchone()[0]
    # get course id
    curr.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (course,))
    curr.execute("SELECT id FROM Course WHERE title = ?", (course,))
    course_id = curr.fetchone()[0]
    # set user and course into member table
    curr.execute("INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)", (user_id,course_id,role,))
conn.commit()