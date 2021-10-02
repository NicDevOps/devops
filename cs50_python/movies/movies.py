import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# show_tables = cursor.execute(".schema").fetchall()

# print(show_tables)

# 1
# rows = cursor.execute("SELECT title FROM movies WHERE year = '2008'").fetchall()
# print(rows)

# 2
# rows = cursor.execute("SELECT birth FROM people WHERE name = 'Emma Stone'").fetchall()
# print(rows)

# 3
# rows = cursor.execute("SELECT title FROM movies WHERE year > 2018 OR year = 2018 ORDER BY year ASC").fetchall()
# print(rows)

# 4
# rows = cursor.execute("SELECT COUNT(rating) FROM ratings where rating = 10.0").fetchall()
# print(rows)

# 5
# rows = cursor.execute("SELECT title, year FROM movies WHERE title LIKE '%Harry Potter%' ORDER BY year ASC").fetchall()
# print(rows)

# 6
# rows = cursor.execute("SELECT AVG(rating) FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012)").fetchall()
# print(rows)

# 7
# rows = cursor.execute("SELECT movie_id, rating FROM ratings WHERE movie_id IN (SELECT id FROM movies WHERE year = 2010) ORDER BY rating DESC").fetchall()
# print(rows)

# 7
# rows = cursor.execute("SELECT movies.title, ratings.rating FROM movies INNER JOIN ratings ON movies.id = ratings.movie_id ORDER BY rating DESC, title ASC").fetchall()
# print(rows)

# 8
# rows = cursor.execute("SELECT people.name FROM ((people INNER JOIN stars ON people.id = stars.person_id) INNER JOIN movies ON stars.movie_id = movies.id) WHERE title = 'Toy Story' UNION SELECT people.name FROM ((people INNER JOIN directors ON people.id = directors.person_id) INNER JOIN movies ON directors.movie_id = movies.id) WHERE title = 'Toy Story'").fetchall()
# print(rows)

query_limit = 3

sql_query = '''
select *
from movies
limit %s;
''' % (query_limit)

rows = cursor.execute(sql_query).fetchall()
print(rows)