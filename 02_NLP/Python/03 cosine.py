import re
import numpy as np
import scipy.spatial

# Сравнение предложений
catsFile = open('./sentences.txt', 'r')

catsText = catsFile.read().lower().split('\n')
print('ПРЕДЛОЖЕНИЯ. ВСЕГО', len(catsText))
print('\n'.join(catsText[0:5]))

catsToken = []  # Строки с разделением на слова
wordDic = dict()  # Словарь частот вхождения слов

for sent in catsText:
    tmpStr = re.split('[^a-z]', sent)  # Разбиваем на слова, без символов
    strKey = []
    for key in tmpStr:  # Очищаем массив от пустых элементов
        if key:
            strKey.append(key)
            wordDic.setdefault(key)  # Формируем словарь
    catsToken.append(strKey)
print('\nТОКЕНЫ ПРИЛОЖЕНИЙ')
print(catsToken[0:5])

index = 0
for key in wordDic:  # Проставляем индекс у каждого слова
    wordDic[key] = index
    index += 1
print('\nСЛОВАРЬ. ВСЕГО', len(wordDic))
print(wordDic)

wordInclude = np.zeros((len(catsText),len(wordDic)))  # Массив размерностью строк и числа встреченных слов
sentInd = 0
for sentence in catsToken:
    for word in sentence:
        wordInclude[sentInd][wordDic[word]] += 1
    sentInd += 1
print('ВЕКТОР ПЕРВОГО ПРЕДЛОЖЕНИЯ. ДЛИНА ВЕКТОРА', len(wordInclude[0]))
print(wordInclude[0])

dists = []
for row in wordInclude:
    dists.append(scipy.spatial.distance.cosine(wordInclude[0,:], row))
print('\nДИСТАНЦИИ МЕЖДУ ПРЕДЛОЖЕНИЯМИ')
print(dists[0:5])

i = 0
min1 = 1
min2 = 1
i1 = 0
i2 = 0
for value in dists:  # Ищем минимальных два индекса, ближайших и их значнеия
    if (value != 0.) & (value < min1):
        min2 = min1
        min1 = value
        i2 = i1
        i1 = i
    i += 1
print('\nИСКОМАЯ СТРОКА:', 0, 'ДИСТАНЦИЯ:', 0, '\n', catsText[0])
print('\nБЛИЖАЙШАЙШАЯ СТРОКА:', i1, 'ДИСТАНЦИЯ:', min1, '\n', catsText[i1])
print('\nБЛИЖАЙШАЙШАЯ СТРОКА2:', i2, 'ДИСТАНЦИЯ:', min2, '\n', catsText[i2])