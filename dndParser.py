import random

import requests
from bs4 import BeautifulSoup as bs


def search(pred):
    try:
        # URL_TEMPLATE = "https://dnd.su/articles/bestiary/?search=" + pred[pred.find("бестиарий") + 11:len(pred)]
        # print(URL_TEMPLATE)
        # r = requests.get(URL_TEMPLATE)
        # print(r.status_code)
        #
        # soup = bs(r.text, "html.parser")
        # vacancies_names = soup.find_all('h2', class_='card-title',itemprop='name')
        # print(vacancies_names)
        #
        # URL = "https://dnd.su" + vacancies_names[0].a['href']
        URL = "https://dnd.su/bestiary/?search=" + pred[pred.find("бестиарий") + 11:len(pred)]
        return URL
    except:
        return 'Не найдено'
    # r = requests.get(URL)
    # soup = bs(r.text, "html.parser")
    # rt = soup.find_all('div', class_='desc')
    # text = ''
    # for i in rt:
    #     text = text + i.text
    # print(text)
    # return text

def randomCreature():
    names = []
    with open('dndCreature.txt', 'r', encoding='UTF-8') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            names.append(x)
    return names[random.randint(0, 2382)]
