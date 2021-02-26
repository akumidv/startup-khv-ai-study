import nltk
from nltk.stem.snowball import SnowballStemmer

phrase = 'Если вы не можете объяснить это своей бабушке, вы сами этого не понимаете'

tokens = nltk.word_tokenize(phrase, language="russian")
print(tokens)

snowballStemmer = SnowballStemmer('russian')
stemmer = [snowballStemmer.stem(word) for word in tokens]
print('\nСтеммы', stemmer)
