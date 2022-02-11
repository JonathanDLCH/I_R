import re
import string
from nltk.corpus import stopwords
from nltk.stem import *

file = open('Texto1.txt','rt')
text = file.read().lower()

words1=text.split()
words2=text.split()

#Primera forma de quitar simbolos
words1 = re.split(r'\W+',text)
print(words1[:100])

#Segunda forma de quitar simbolos
print(string.punctuation)
re_punc = re.compile('[%s]'%re.escape(string.punctuation))
stripped = [re_punc.sub('',w) for w in words2]
print(stripped[:100])

#longitud de las cadenas
print('word:',len(words1),'stripped:',len(stripped))

#Palabras vacias en ingles
stop_words = stopwords.words('english')
#print(stop_words)

cln_words = list()
for word in stripped[:100]:
    if(word not in stop_words):
        cln_words.append(word)

#PorterStemmer
print('\nPorterStemmer')
porter = PorterStemmer()
porterWords = [porter.stem(word) for word in cln_words]
print(' '.join(porterWords))

#Snowball
print('\nSnowball')
print('Lenguajes soportados:')
print(" ".join(SnowballStemmer.languages))
snowball = SnowballStemmer("english")
snowball2 = SnowballStemmer("english", ignore_stopwords=True)
Snowballwords = [snowball.stem(word) for word in cln_words]
print(' '.join(Snowballwords))

#wordnet
print('\nwordnet')
wnl = WordNetLemmatizer()
wnlwords = [wnl.lemmatize(word) for word in cln_words]
print(' '.join(wnlwords))

file.close()