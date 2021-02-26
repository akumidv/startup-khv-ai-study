const fs = require('fs')
const talismanTokenaizer = require('talisman/tokenizers/words/treebank'); // treebank Для англ.языка - разбивает в т.ч. сокращения
// const talismanTokenaizer = require('talisman/tokenizers/words/naive') // naive без знаков припинания

const cosine = require('talisman/metrics/cosine')

// https://github.com/akumidv/math-phyton/blob/master/7-11.programmir.ipynb

const catsFile = fs.readFileSync('./sentences.txt').toString().toLowerCase()
const catsText = catsFile.split('\n')
console.log(`\nПРЕДЛОЖЕНИЯ. ВСЕГО ${catsText.length}`)
console.log(catsText.slice(0,5))


const catSentenceTokens = catsText
  .map(sentence => talismanTokenaizer(sentence).filter(item => /^[a-z]/.test(item)))
console.log(`\nТОКЕНЫ ПРИЛОЖЕНИЙ`)
console.log(catSentenceTokens.slice(0,1))


const catTextTokens = talismanTokenaizer(catsFile)
  .filter((word, i, arr) => /^[a-z]/.test(word) && arr.indexOf(word) === i)
console.log(`\nВСЕ ТОКЕНЫ. ВСЕГО ${catTextTokens.length}`)
console.log(catTextTokens.slice(0,10))


const wordDic = {}
// catTextTokens.forEach((item, index) => wordDic[item] = index)
let index = 0
catSentenceTokens.forEach(sentence => {
  sentence.forEach((word) => typeof wordDic[word] === 'undefined' ?
    wordDic[word] = index++ : wordDic[word])
})
console.log(`\nСЛОВАРЬ. ВСЕГО ${Object.keys(wordDic).length}`)
index = 0
for(let key in wordDic) {
  console.log(`  ${key}:${wordDic[key]}`)
  if (index++ > 10) break
}

const wordInclude = catSentenceTokens.map(sentence => {
  const sentenceRow = Object.keys(wordDic).map(() => 0)
  sentence.forEach(word => sentenceRow[wordDic[word]]++)
  return sentenceRow
})
console.log(`\nВЕКТОР ПЕРВОГО ПРЕДЛОЖЕНИЯ. ДЛИНА ВЕКТОРА ${wordInclude[0].length}`)
console.log(wordInclude[0])

const dist = wordInclude.map(sentence => (1 - cosine(wordInclude[0], sentence)))
console.log('\nДИСТАНЦИИ МЕЖДУ ПРЕДЛОЖЕНИЯМИ')
console.log(dist.slice(0,5))

const minVal = dist.concat().sort((a,b) => a-b)
console.log('\nИСКОМАЯ СТРОКА:', 0, 'ДИСТАНЦИЯ:', 0, '\n', catsText[0])
console.log('\nБЛИЖАЙШАЙШАЯ СТРОКА:', dist.indexOf(minVal[1]), 'ДИСТАНЦИЯ:', minVal[1], '\n', catsText[dist.indexOf(minVal[1])])
console.log('\nБЛИЖАЙШАЙШАЯ СТРОКА2:', dist.indexOf(minVal[2]), 'ДИСТАНЦИЯ:', minVal[2], '\n', catsText[dist.indexOf(minVal[2])])
