import sqlite3
from contextlib import closing

connection = sqlite3.connect("songs.db")

# print(connection.total_changes)

cursor = connection.cursor()

#  write a SQL query to list the names of all songs in the database.
rows = cursor.execute("SELECT name FROM songs").fetchall()
print(rows)

# write a SQL query to list the names of all songs in increasing order of tempo.
rows = cursor.execute("SELECT name FROM songs ORDER BY tempo").fetchall()
print(rows)

# write a SQL query to list the names of the top 5 longest songs, in descending order of length.
rows = cursor.execute("SELECT name FROM songs ORDER BY duration_ms DESC LIMIT 5").fetchall()
print(rows)

# write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75.
rows = cursor.execute("SELECT name FROM songs WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75").fetchall()
print(rows)

# write a SQL query that returns the average energy of all the songs.
rows = cursor.execute("SELECT AVG(energy) FROM songs").fetchall()
print(rows)

# write a SQL query that lists the names of songs that are by Post Malone.
rows = cursor.execute("SELECT name FROM songs WHERE artist_id = (SELECT id FROM artists WHERE name = 'Post Malone')").fetchall()
print(rows)

# write a SQL query that returns the average energy of songs that are by Drake.
rows = cursor.execute("SELECT AVG(energy) FROM songs WHERE artist_id = (SELECT id FROM artists WHERE name = 'Drake')").fetchall()
print(rows)

# write a SQL query that lists the names of the songs that feature other artists.
rows = cursor.execute("SELECT name FROM songs WHERE name LIKE '%feat.%'").fetchall()
print(rows)

with closing(sqlite3.connect("songs.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)