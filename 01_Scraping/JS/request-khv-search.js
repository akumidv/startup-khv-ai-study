const superagent = require('superagent');
const cheerio = require('cheerio');

(async () => {
  try {
    const search = await superagent
      .get('https://todaykhv.ru/search/?q=%D0%94%D0%92%D0%96%D0%94&s=') // ДВЖД
    const htmlSearch = search.res.text
    $ = cheerio.load(htmlSearch);

    const searchHeads = $('.search-page .searchNewsHead')

    console.log(`Поиск заголовков: ${searchHeads.length}`)

    let headersAndUrl = []
    searchHeads.each((i, el) => {
      headersAndUrl.push({head: $(el).text(), url: $(el).attr('href')});
    })

    console.log('Заголовки и ссылки статей')
    console.log(headersAndUrl)
  } catch(e) {
    console.error(e)
  }

})();

