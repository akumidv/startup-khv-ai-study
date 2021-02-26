const natural = require('natural');

const greet = ['Привет', 'Здравствуй', 'Добрый день',
  'Добрый вечер', 'Здравствуйте', 'Приветствую',
  'Здорова', 'Доброе утро']

const bye = ['Пока', 'До встречи', 'До свидания',
  'Прощай', 'Еще увидимся', 'скоро увидимся', 'до новых встречь',
  'Дотвиданья']

const classifier = new natural.BayesClassifier(natural.PorterStemmerRu);

greet.forEach(item => classifier.addDocument(item, 'Приветствие'))
bye.forEach(item => classifier.addDocument(item, 'Прощание'))

classifier.train();

const w1 = 'Добрых суток'
const w2 = 'Покедова'
const w3 = 'Увидимся'

console.log('Мешок слов', classifier.features)

console.log(`Для ${w1} ожидаем приветствие:`, classifier.classify(w1));
console.log('Вероятности', classifier.getClassifications(w1));

console.log(`Для ${w2} ожидаем  прощание:`, classifier.classify(w2));
console.log(classifier.getClassifications(w2));

console.log(`Для ${w3} ожидаем  прощание:`, classifier.classify(w3));
console.log('Вероятности', classifier.getClassifications(w3));
