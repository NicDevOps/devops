# sqlite3 python3 tutorial 

import sqlite3
from contextlib import closing

connection = sqlite3.connect("aquarium.db")

print(connection.total_changes)

cursor = connection.cursor()
# cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")

# cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
# cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

# target_fish_name = "Jamie"
# rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = ?",
# (target_fish_name,),
# ).fetchall()
# print(rows)

# new_tank_number = 2
# moved_fish_name = "Sammy"
# cursor.execute(
#     "UPDATE fish SET tank_number = ? WHERE name = ?",
#     (new_tank_number, moved_fish_name)
# )

# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

# # release sammy into the wild ;)

# released_fish_name = "Sammy"
# cursor.execute(
#     "DELETE FROM fish WHERE name = ?",
#     (released_fish_name,)
# )

# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)


# cursor.execute(
#     "INSERT INTO fish (name, species, tank_number) VALUES (?, ?, ?)",
#     (name, species, tank_number)
# )

# rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
# print(rows)

# name = 'Dori'
# species = 'surgeon_fish'
# tank_number = 8

# with closing(sqlite3.connect("aquarium.db")) as connection:
#     with closing(connection.cursor()) as cursor:
        # rows = cursor.execute("SELECT 1").fetchall()
        # print(rows)

        # cursor.execute(
        #     "INSERT INTO fish (name, species, tank_number) VALUES (?, ?, ?)",
        #     (name, species, tank_number)
        # )

        # result = cursor.execute(
        #     "SELECT name, species, tank_number FROM fish"
        # ).fetchall()


        # print(result)
