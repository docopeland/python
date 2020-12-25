# Musical Track Database
# This application will read an iTunes export file in XML and produce a properly normalized database with this
# structure:
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
#
# For the database that you turn in for this assignment, only use the Library.xml data that is provided.
#
# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it
# expects to see:
# SELECT Track.title, Artist.name, Album.title, Genre.name
#     FROM Track JOIN Genre JOIN Album JOIN Artist
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3

import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("tracks.sqlite")
curr = conn.cursor()

# drop and create tables
curr.executescript("""
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER,
    genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)""")

# get the info out of the file
xmlName = input("Enter XML: ")
if len(xmlName) < 1: xmlName = "files/Library.xml"
data = ET.parse(xmlName)
info = data.findall("dict/dict/dict")

# find the correct value from the xml
def lookup(d, keyword):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == keyword:
            found = True
    return None

#looping through the entries of the xml
print("There are",len(info),"tracks")
for entry in info:
    if lookup(entry,"Track ID") is None: continue
    name = lookup(entry,"Name")
    artist = lookup(entry,"Artist")
    album = lookup(entry,"Album")
    genre = lookup(entry,"Genre")
    time = lookup(entry,"Total Time")
    count = lookup(entry,"Play Count")
    rating = lookup(entry,"Rating")
    if name is None or artist is None or album is None or genre is None: continue
    print(name, artist, album, genre, time, count, rating)

    # getting artist_id
    curr.execute("INSERT OR IGNORE INTO Artist (name) VALUES ( ? )", (artist,))
    curr.execute("SELECT id FROM Artist where name = ?", (artist,))
    artist_id = curr.fetchone()[0]

    # getting genre_id
    curr.execute("INSERT OR IGNORE INTO Genre (name) VALUES ( ? )", (genre,))
    curr.execute("SELECT id FROM Genre where name = ?", (genre,))
    genre_id = curr.fetchone()[0]

    # getting album_id
    curr.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )", (album,artist_id,))
    curr.execute("SELECT id FROM Album where title = ?", (album,))
    album_id = curr.fetchone()[0]

    # doing the track
    curr.execute("""INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
    VALUES ( ? , ? , ? , ? , ? , ? )""", (name,album_id,genre_id,time,rating,count,))
conn.commit()