import sqlite3
import requests
from bs4 import BeautifulSoup


def get_all_cities():
    page = requests.get('https://города-россия.рф/alphabet.php', verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find('div', {'class': "common-text"}).find('ul').find_all('li')
    result = [element.text for element in result]
    return result

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

# query = '''CREATE TABLE city (id integer PRIMARY KEY, name text)'''
# query = """DROP TABLE city"""
# # query ="INSERT INTO city (name) VALUES ('SPB')"
# query = "SELECT * FROM sqlite_master WHERE type='table'"
# # query = "UPDATE city SET name = 'Samara' where id=4"
# # query = "DELETE FROM city where id=1"
# #
# # cursor.execute(query)
#
# cities = get_all_cities()
# print(cities)
# for city in cities:
#     query = f"INSERT INTO main_city(name) VALUES ('{city}')"
#     cursor.execute(query)
#     connection.commit()

query = f"SELECT * FROM main_city"
cursor.execute(query)
connection.commit()
data = cursor.fetchall()
print(data)


connection.close()