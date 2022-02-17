import re
import string
from typing import TextIO
import nltk
from nltk.corpus import stopwords
from nltk.stem import *
from nltk.tokenize import word_tokenize

file = open('files-merged.txt','rt')
text = file.read().lower()
words1=text.split('\n')
doc=open("TRUNCAMIENTO.txt",'w')
doc1=open("LEMATIZACION.txt",'w')
print(words1)
#ELIMINAR SIMBOLOS

re_punc = re.compile('[%s]'%re.escape(string.punctuation))
stripped = [re_punc.sub('',w) for w in words1]
#print(stripped)
#elimina palabras vacias
#stop_words = stopwords.words('english')
#tokens_without_sw = [word for word in stripped if not word in stopwords.words()]
#print(tokens_without_sw)
stop_words = stopwords.words('english')
#print(stop_words)
cln_words = list()
for paragraph in stripped:
    for word in paragraph:
        if(word not in stop_words):
            cln_words.append(word)
#print(cln_words)

#TRUNCAMIENTO
porter = PorterStemmer()
porterWords = [porter.stem(word) for word in cln_words]
doc.write(str(porterWords))

#LEMATIZACION
wnl = WordNetLemmatizer()
wnlwords = [wnl.lemmatize(word) for word in cln_words]
doc1.write(str(wnlwords))