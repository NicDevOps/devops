import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# query_limit = 3

# sql_query = '''
# select *
# from movies
# limit %s;
# ''' % (query_limit)

# 1 G
# sql_query = '''
# SELECT title
# FROM movies
# WHERE year = '2008';
# '''

# 2 G
# sql_query = '''
# SELECT birth
# FROM people 
# WHERE name = 'Emma Stone';
# '''

# 3 G
# sql_query = '''
# SELECT title 
# FROM movies 
# WHERE year > 2018 OR year = 2018 
# ORDER BY year ASC;
# '''

# 4 G
# sql_query = '''
# SELECT rating
# FROM ratings 
# WHERE rating = 10.0;
# '''

# 5 G
# sql_query = '''
# SELECT title, year 
# FROM movies 
# WHERE title 
# LIKE 'Harry Potter%' 
# ORDER BY year ASC;
# '''

# 6 G
# sql_query = '''
# SELECT AVG(rating) 
# FROM ratings 
# WHERE movie_id 
# IN (SELECT id FROM movies WHERE year = 2012);
# '''

# 7 G
# sql_query = '''
# SELECT movies.title, ratings.rating 
# FROM movies 
# INNER JOIN ratings 
# ON movies.id = ratings.movie_id
# WHERE year = '2010' 
# ORDER BY rating DESC, title ASC;
# '''

# 8 G
# sql_query = '''
# SELECT name 
# FROM people
# WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE title = 'Toy Story'))
# '''

# 9 G
# sql_query = '''
# SELECT DISTINCT people.id, people.name
# FROM stars
# JOIN movies on stars.movie_id = movies.id
# JOIN people on stars.person_id = people.id
# WHERE movies.year = '2004'
# '''

# 10 G
# sql_query = '''
# SELECT DISTINCT directors.person_id, name
# FROM people
# JOIN directors ON people.id = directors.person_id
# JOIN ratings ON directors.movie_id = ratings.movie_id
# WHERE rating >= 9.0
# '''

# 11 G
# sql_query = '''
# SELECT title
# FROM movies
# WHERE id IN (SELECT movie_id FROM ratings 
# WHERE movie_id IN (SELECT movie_id FROM stars 
# WHERE person_id IN (SELECT id FROM people WHERE name = 'Chadwick Boseman')))
# LIMIT 5
# '''

# 12 G
# sql_query = '''
# SELECT title FROM movies
#     JOIN stars AS s1 ON id = s1.movie_id
#     JOIN stars AS s2 ON id = s2.movie_id
#     WHERE s1.person_id IN (SELECT id FROM people WHERE name = 'Helena Bonham Carter') 
#     AND s2.person_id IN (SELECT id FROM people WHERE name = 'Johnny Depp')
# '''

# 13
# sql_query = '''
# SELECT people.id, name
# FROM people
# WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'))))
# OR id IN (SELECT person_id FROM directors WHERE movie_id IN (SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'))))
# '''

sql_query = '''
SELECT distinct people.id, name
FROM people
WHERE id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE id IN (SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = '1958'))))
and people.id != '102'
'''

###########################

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
# OR id IN (SELECT person_id FROM stars WHERE movie_id IN (SELECT id FROM movies WHERE year = '2004'))
# ORDER BY birth
# '''

# sql_query = '''
# select name, birth
# from people
# LEFT join stars on stars.person_id = people.id
# join directors on directors.person_id = people.id
# join movies on stars.movie_id = movies.id or directors.movie_id = movies.id
# where movies.year = '2004'
# '''

# sql_query = '''
# SELECT DISTINCT name 
# FROM people
# WHERE id = (SELECT person_id FROM stars WHERE movie_id = (SELECT movie_id FROM ratings WHERE rating >= '9.0'))
# OR id = (SELECT person_id FROM directors WHERE movie_id = (SELECT movie_id FROM ratings WHERE rating >= '9.0'))
# '''


rows = cursor.execute(sql_query).fetchall()
print(rows)
print(len(rows))

