from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from itertools import chain

greet = ['Привет', 'Здравствуй', 'Добрый день',
  'Добрый вечер', 'Здравствуйте', 'Приветствую',
  'Здорова', 'Доброе утро']

bye = ['Пока', 'До встречи', 'До свидания',
  'Прощай', 'Еще увидимся', 'скоро увидимся', 'до новых встречь',
  'Дотвиданья']


trainlist = ([(word, 'greet') for word in greet] +
                [(word, 'bye') for word in bye])

vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in trainlist]))
print('СЛОВАРЬ СЛОВ')
print(vocabulary)

feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in trainlist]

classifier = NaiveBayesClassifier.train(feature_set)
# classifier.show_most_informative_features()


w1 = 'Добрых суток'
w2 = 'Покедова'
w3 = 'Увидимся'

print()
featurized_test_sentence_w1 = {i:(i in word_tokenize(w1.lower())) for i in vocabulary}
print('Для', w1, 'ожидаем приветствие:', classifier.classify(featurized_test_sentence_w1))

featurized_test_sentence_w2 = {i:(i in word_tokenize(w2.lower())) for i in vocabulary}
print('Для', w2, 'ожидаем прощание:', classifier.classify(featurized_test_sentence_w2))

featurized_test_sentence_w3 = {i:(i in word_tokenize(w3.lower())) for i in vocabulary}
print('Для', w3, 'ожидаем прощание:', classifier.classify(featurized_test_sentence_w3))

