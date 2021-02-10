import scrapy
# from TodaykhvItem.items import TodaykhvItem

class TodaykhvSpider(scrapy.Spider):

    name = 'todaykhv'
    allowed_domains = ["todaykhv.ru"]
    start_urls = ["http://todaykhv.ru/"]

    def start_requests(self):
        urls = [
            'http://todaykhv.ru/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) # Есть на puppeteer

    def parse(self, response):
        newsHeads = response.css('.itemNewsWrap .itemNewsHead > a::text')

        firstHeadText = newsHeads.extract_first()

        print('\n\n')
        print('Главная, заголовков:', len(newsHeads))
        print('Заголовок первого элемента:', firstHeadText)
        print('\n\n')

