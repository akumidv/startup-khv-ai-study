const superagent = require('superagent');
const cheerio = require('cheerio');

(async () => {
  try {
    const home = await superagent
      .get('https://todaykhv.ru/')

    const htmlHome = home.res.text
    let $ = cheerio.load(htmlHome);

    const newsHeads = $('.itemNewsWrap .itemNewsHead > a')
    const firstHeadText = newsHeads.first().text()

    console.log(`Главная заголовков: ${newsHeads.length}`)
    console.log(`Заголовок первого элемента: ${firstHeadText}\n`)

  } catch(e) {
    console.error(e)
  }
})();

