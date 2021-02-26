const path = require('path');
const fastText = require('fasttext');

let DATA_PATH = path.resolve(path.join(__dirname, './review_tone.train.txt'));
let MODEL_PATH = path.resolve(path.join(__dirname, './review_model'));
let MODEL_RDY_PATH = path.resolve(path.join(__dirname, './rzd_tone_model.bin'));

const comment = 'Очень жарко. 28 градусов. A из окна дует холод. Особенно на нижней полке.'
// А если порядок слов поменять?
// А пару слов на позитивные?
// const comment = 'очень плохо'
// const comment = 'ужасно'

let classifier = new fastText.Classifier();

(async () => {
  console.log('ОБУЧАЕМ')
  await classifier
    .train('supervised', {
      input: DATA_PATH,
      output: MODEL_PATH,
      epoch: 5
    })
    .then((res) => {
      console.log('Данные о модели:', res)
    });

  console.log('РЕЗУЛЬТАТ ОБУЧЕНИЯ')
  await classifier.predict(comment.toLowerCase().split('\n').join(' '), 5)
    .then((res) => {
      console.log(res)
    });

  console.log('ПРЕДВАРИТЕЛЬНО ОБУЧЕННЫЙ')
  const classifierRdy = new fastText.Classifier(MODEL_RDY_PATH);
  await classifierRdy.predict(comment.toLowerCase().split('\n').join(' '), 5)
    .then((res) => {
      console.log(res)
    });

})()
