import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# query_limit = 3

# sql_query = '''
# select *
# from movies
# limit %s;
# ''' % (query_limit)

# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 1
# sql_query = '''
# SELECT title
# FROM movies
# WHERE year = '2008';
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 2
# sql_query = '''
# SELECT birth
# FROM people 
# WHERE name = 'Emma Stone';
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 3
# sql_query = '''
# SELECT title 
# FROM movies 
# WHERE year > 2018 OR year = 2018 
# ORDER BY year ASC;
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 4
# sql_query = '''
# SELECT COUNT(rating)
# FROM ratings 
# WHERE rating = 10.0;
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 5
# sql_query = '''
# SELECT title, year 
# FROM movies 
# WHERE title 
# LIKE '%Harry Potter%' 
# ORDER BY year ASC;
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 6
# sql_query = '''
# SELECT AVG(rating) 
# FROM ratings 
# WHERE movie_id 
# IN (SELECT id FROM movies WHERE year = 2012);
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 7
# sql_query = '''
# SELECT movies.title, ratings.rating 
# FROM movies 
# INNER JOIN ratings 
# ON movies.id = ratings.movie_id 
# ORDER BY rating DESC, title ASC;
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 8
# sql_query = '''
# SELECT people.name 
# FROM ((people INNER JOIN stars ON people.id = stars.person_id) 
# INNER JOIN movies ON stars.movie_id = movies.id) 
# WHERE title = 'Toy Story' 
# UNION 
# SELECT people.name 
# FROM ((people INNER JOIN directors ON people.id = directors.person_id) 
# INNER JOIN movies ON directors.movie_id = movies.id) 
# WHERE title = 'Toy Story';
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)

# 9
# sql_query = '''
# SELECT DISTINCT name, birth
# FROM people 
# JOIN stars ON people.id = stars.person_id 
# JOIN movies ON stars.movie_id = movies.id
# WHERE year = '2004'
# UNION
# SELECT DISTINCT name, birth
# FROM people 
# JOIN directors ON people.id = directors.person_id
# JOIN movies ON directors.movie_id = movies.id
# WHERE year = '2004'
# ORDER BY birth
# '''

# sql_query = '''
# SELECT DISTINCT name
# FROM people
# WHERE id IN (SELECT person_id FROM directors WHERE movie_id IN (SELECT id FROM movies WHERE year = '2004'))
# AND id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE year = '2004'))
# ORDER BY birth
# '''
# rows = cursor.execute(sql_query).fetchall()
# print(rows)


# 10
# sql_query = '''
# SELECT DISTINCT name 
# FROM people
# JOIN directors ON people.id = directors.person_id
# JOIN ratings ON directors.movie_id = ratings.movie_id
# WHERE rating >= '9.0'
# '''

# 11
# sql_query = '''
# SELECT title
# FROM movies
# WHERE id IN (SELECT movie_id FROM ratings 
# WHERE movie_id IN (SELECT movie_id FROM stars 
# WHERE person_id IN (SELECT id FROM people WHERE name = 'Chadwick Boseman')))
# LIMIT 5
# '''

# 12
# sql_query = '''
# SELECT title
# FROM movies
# WHERE id IN (SELECT movie_id FROM stars 
# WHERE person_id IN (SELECT id FROM people WHERE name = 'Helena Bonham Carter' AND name = 'Johnny Depp'))
# '''

# 13
sql_query = '''
SELECT ALL name
FROM people
WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'))))
OR id IN (SELECT person_id FROM directors WHERE movie_id IN (SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'))))
'''
rows = cursor.execute(sql_query).fetchall()
print(rows)

