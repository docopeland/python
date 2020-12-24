# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
#
# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with different files, make sure to empty out the data before
# each run.
#
# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
#
# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.
#
# Because the sample code is using an UPDATE statement and committing the results to the database as each record is
# read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely
# writing all the data to disk every time it is called.
#
# The program can be sped up greatly by moving the commit operation outside of the loop. In any database program,
# there is a balance between the number of operations you execute between commits and the importance of not losing the
# results of operations that have not yet been committed.

import sqlite3
import urllib.request, urllib.parse, urllib.error
import re

# open and read the file
file = input("Enter file: ")
if len(file) < 1: file = "files/mbox-short.txt"
fOpen = open(file)

# open and connect to the db
conn = sqlite3.connect("sql2.sqlite")
curr = conn.cursor()

# if table exists, delete it then make a new one
curr.execute("DROP TABLE IF EXISTS Counts")
curr.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

for line in fOpen:
    # find the email domains
    if not line.startswith("From: "): continue
    else: email = line.split()[1].split("@")[1]
    # see if the email domain is already in the db
    curr.execute("SELECT * FROM Counts WHERE org = ?", (email,))
    row = curr.fetchone()
    if row is None:
        curr.execute("INSERT INTO Counts (org, count) VALUES (?,1)", (email,))
    else:
        curr.execute("UPDATE Counts SET count = count + 1 where org = ?", (email,))
conn.commit()
