from bs4 import BeautifulSoup
import requests

home = requests.get('https://todaykhv.ru/')
htmlHome = home.text

soup = BeautifulSoup(htmlHome, 'html.parser')

newsHeads = soup.select('.itemNewsWrap .itemNewsHead > a')
firstHeadText = newsHeads[0].text

print('Главная, заголовков:', len(newsHeads))
print('Заголовок первого элемента:', firstHeadText)
