from bs4 import BeautifulSoup
import requests


def get_all_cities():
    page = requests.get('https://xn----7sbiew6aadnema7p.xn--p1ai/alphabet.php', verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    # print(page.text)

    result = soup.find('div', {'class': "common-text"}).find("ul").find_all('li')
    result = [element.text for element in result]
    return result
