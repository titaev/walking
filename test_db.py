# import sqlite3
#
# connection = sqlite3.connect('example.db')
# cursor = connection.cursor()
#
# # query = '''CREATE TABLE city (id integer PRIMARY KEY, name text)'''
# # query = '''DROP TABLE city'''
# # query = "INSERT INTO city (name) VALUES ('Volgograd')"
# # query = "INSERT INTO city (id, name) VALUES (1, 'Moscow')"
# query = "SELECT * FROM city"
# # query = "SELECT * FROM city WHERE id=1"
# # query = "UPDATE city SET name = 'Samara' WHERE id=1"
# # query = "DELETE FROM city WHERE name='Samara'"
#
#
# cursor.execute(query)
#
# cities = cursor.fetchall()
# print(cities)
#
# connection.commit()
# connection.close()
