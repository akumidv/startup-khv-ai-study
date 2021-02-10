from bs4 import BeautifulSoup
import requests

search = requests.get('https://todaykhv.ru/search/?q=%D0%94%D0%92%D0%96%D0%94&s=')
htmlSearch = search.text

soup = BeautifulSoup(htmlSearch, 'html.parser')

searchHeads = soup.select('.search-page .searchNewsHead')
print('Поиск заголовков:', len(searchHeads))

headersAndUrl = []

for headers in searchHeads:
  headersAndUrl.append({'head': headers.text, 'url': headers.get('href')})

print('Заголовки и ссылки статей')
print(headersAndUrl)
