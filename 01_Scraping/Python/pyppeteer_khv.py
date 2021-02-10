import asyncio
from pyppeteer import launch

async def extract_all():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://todaykhv.ru/')

    await page.waitForSelector('.itemNewsWrap .itemNewsHead > a', timeout=10000)
    newsHeads = await page.JJ('.itemNewsWrap .itemNewsHead > a')

    firstHeadText = await page.evaluate('el => el.innerText', newsHeads[0])

    print('Главная, заголовков:', len(newsHeads))
    print('Заголовок первого элемента:', firstHeadText)

    await browser.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(extract_all())
