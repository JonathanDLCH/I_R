from pickle import FALSE
import re
import string
from nltk.corpus import stopwords

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
print('Palabras vacias')
print(stop_words[:10])

cln_words = list()
for word in stripped[:100]:
    if(word not in stop_words):
        cln_words.append(word)

print('Lista final')
print(cln_words)
file.close()