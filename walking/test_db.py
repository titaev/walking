# import sqlite3
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_all_cities():
#     page = requests.get('https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php', verify=False)
#     soup = BeautifulSoup(page.text, "html.parser")
#     # print(page.text)
#
#     result = soup.find('div', {'class': "common-text"}).find("ul").find_all('li')
#     result = [element.text for element in result]
#     return result
#
# connection = sqlite3.connect('db.sqlite3')
# cursor = connection.cursor()
#
# # cities = get_all_cities()
#
# # for city in cities:
# #     query = f"INSERT INTO main_city (name) VALUES ('{city}')"
# #     cursor.execute(query)
# #     connection.commit()
#
# query = f"SELECT * FROM main_city"
# cursor.execute(query)
# connection.commit()
# data = cursor.fetchall()
# print(data)
#
# connection.close()
#
#





#
# # query = """CREATE TABLE city (id integer PRIMARY KEY, name text)"""
# # query = """DROP TABLE city"""
# query = "SELECT name FROM sqlite_master WHERE type='table'"
# # query = "DELETE FROM city WHERE name='Samara'"
# # query = "INSERT INTO city (id, name) VALUES (1, 'sdffgwerg')"
# # query = "UPDATE city SET name = 'Samara' WHERE id=1"
#
# cursor.execute(query)
# #
# cities = cursor.fetchall()
# print(cities)

# connection.commit()
# connection.close()
