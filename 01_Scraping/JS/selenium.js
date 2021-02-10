require('chromedriver');
const {Builder, By, Key, until} = require('selenium-webdriver');

(async () => {
  let driver = await new Builder().forBrowser('chrome').build();
  try {
    await driver.get('https://todaykhv.ru/');

    const newsHeads = await driver.findElements(By.css('.itemNewsWrap .itemNewsHead > a'))
    const firstHeadText = await newsHeads[1].getText();

    console.log(`Главная заголовков: ${newsHeads.length}`);
    console.log(`Заголовок первого элемента: ${firstHeadText}\n`);

  } finally {
    await driver.quit();
  }
})();