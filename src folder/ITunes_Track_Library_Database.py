import sqlite3
import xml.etree.ElementTree as ET

dbname = input("Enter your database file name:")

conn = sqlite3.connect(dbname)
cur = conn.cursor()

count = 0
#Erase existing tables for multiple runs
cur.executescript('''DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track
''')

#Making Artist (id, name), Genre (id, name), Album (id, artist_id, title), Track (id, album_id, genre_id, len)
cur.executescript('''
    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
    );

    CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
    );
''')

fname = input("Enter path to the XML File:")

def lookup(entry, value):
    found = False
    for child in entry:
        if found : return child.text 
        if child.tag == 'key' and child.text == value : #If Track ID is not Null, then found = true for that music entry 
            found = True
    return None   #To check whether the music_entry iterates through the Track ID line
            

stuff = ET.parse(fname)
music_list = stuff.findall('dict/dict/dict')

for music_entry in music_list:

        if(lookup(music_entry, 'Track ID') is None) : continue
        name = lookup(music_entry, 'Name')
        artist = lookup(music_entry, 'Artist')
        album = lookup(music_entry, 'Album')
        genre = lookup(music_entry, 'Genre')
        count = lookup(music_entry, 'Play Count')
        rating = lookup(music_entry, 'Rating')
        length = lookup(music_entry, 'Total Time')

        if name is None or artist is None or album is None or genre is None:
            continue

        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,)) #Makes sure each artist only entered once
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,)) #Selects all the rows with name = artist and creates a temp. table
        artist_id = cur.fetchone()[0] #Selects the 1st row from that table and 1st column value

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, )) 
        album_id = cur.fetchone()[0] #Foreign key is defined as the table is updated

        cur.execute('''INSERT OR IGNORE INTO Genre (name)
            VALUES (?)''', (genre,)) #Since id is AUTOINCREMENT, no need to manually input values
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len) 
        VALUES (?, ?, ?, ? )''', 
        (name, album_id, genre_id, length ) )

conn.commit()






