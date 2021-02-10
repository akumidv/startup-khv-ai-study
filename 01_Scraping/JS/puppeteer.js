const puppeteer = require('puppeteer');
(async () => {
  let browser;
  try {
    browser = await puppeteer.launch({headless: false});
    let page = await browser.newPage();
    await page.goto('https://todaykhv.ru/', {waitUntil: 'load'});

    await page.watiForSelector('.itemNewsWrap .itemNewsHead > a', {timeout: 10000})
    const newsHeads = await page.$$('.itemNewsWrap .itemNewsHead > a')
    const firstHeadText = await newsHeads[0].evaluate(el => el.innerText)

    console.log(`Всего заголовков: ${newsHeads.length}`)
    console.log(`Заголовок первого элемента: ${firstHeadText}`)

  } catch(e) {
     console.error(e)
  } finally {
    await browser.close();
  }
})();

