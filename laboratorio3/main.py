"""
Aplicando truncamiento y lematizacion con nltk
"""
from nltk.corpus import stopwords
from nltk.stem import *
import re
import string

def delete_stopwords(paragraphs):
    """
    Funcion que nos permite estructurar el texto,
    quitamos simbolos y palabras vacias.
    """
    re_punc = re.compile('[%s]'%re.escape(string.punctuation))
    letters = [re_punc.sub('',w) for w in paragraphs]
    letters=[line.split() for line in letters]

    #Palabras vacias en ingles
    stop_words = stopwords.words('english')
    cln_words = list()
    for word in letters:
        for e in word:
            if(e not in stop_words):
                cln_words.append(e)

def truncamiento(words):
    #PorterStemmer
    print('\nPorterStemmer')
    porter = PorterStemmer()
    porterWords = [porter.stem(word) for word in words]
    print(' '.join(porterWords))

def lematizacion(words):
    wnl = WordNetLemmatizer()
    wnlwords = [wnl.lemmatize(word) for word in words]
    print(' '.join(wnlwords))

    

file = open('files-merged.txt','rt')
content = file.read().lower()
paragraph = content.split('\n')

delete_stopwords(paragraph)
