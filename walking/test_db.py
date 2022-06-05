import sqlite3
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def get_cities():
    page = requests.get("https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php", verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find("div", {"class": "common-text"}).find("ul").find_all("li")
    result = [element.text for element in result]
    return result


connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
# cities = get_cities()
# for city in cities:
#     query = f"INSERT INTO main_city (name) VALUES ('{city}')"
#     cursor.execute(query)
#     connection.commit()

query = f"SELECT * FROM main_city"
cursor.execute(query)
connection.commit()
data = cursor.fetchall()
print(data)

connection.close()


# query = """CREATE TABLE city (id INTEGER PRIMARY KEY, name TEXT)"""
# query = """INSERT INTO city (name) VALUES ('Volgograd')"""
# query = """DROP TABLE city"""
# query = "SELECT * FROM main_city"
# query = "UPDATE city SET name = 'Samara' WHERE  id=1"
# query = "DELETE FROM city WHERE name='Samara'"
# query = "SELECT name FROM sqlite_master WHERE type='table'"
#
# cursor.execute(query)
#
# cities = cursor.fetchall()
# print(cities)
# connection.commit()
# connection.close()
