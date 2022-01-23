import sqlite3
from pprint import pprint

connection = sqlite3.connect("finance.db")

cursor = connection.cursor()

sql_query = '''
SELECT * FROM stocks
'''
rows = cursor.execute(sql_query).fetchall()

if not rows:
    print("ok")

print(rows)
# pprint(rows)
# print(len(rows))
