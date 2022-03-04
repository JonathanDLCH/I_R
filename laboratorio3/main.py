"""
Aplicando truncamiento y lematizacion con nltk
"""
from nltk.corpus import stopwords
from nltk.stem import *
import re
import string

def delete_stopwords(dic_documentos):
    """
    Funcion que nos permite estructurar el texto,
    quitamos simbolos y palabras vacias.
    """
    for llave in dic_documentos:
        documento = dic_documentos[llave]
        re_punc = re.compile('[%s]'%re.escape(string.punctuation))
        documentoaux=""
        for word in documento:
            if word not in re_punc.sub('',word):
                continue
            else:
                documentoaux=documentoaux+word

        dic_documentos[llave]=documentoaux
        
        #Palabras vacias en ingles
        stop_words = stopwords.words('english')
        documentoaux = documentoaux.split(' ')
        documentoaux2=""
        for word in documentoaux:
            if word not in stop_words:
                documentoaux2=documentoaux2+' '+word

        dic_documentos[llave]=documentoaux2
    create_file('woutSW',dic_documentos)

def truncamiento(words):
    #PorterStemmer
    print('\nPorterStemmer')
    porter = PorterStemmer()
    porterWords = [porter.stem(word) for word in words]
    print(' '.join(porterWords))
    create_file('truncamiento',porterWords)

def lematizacion(words):
    wnl = WordNetLemmatizer()
    wnlwords = [wnl.lemmatize(word) for word in words]
    print(' '.join(wnlwords))
    create_file('lematizacion',wnlwords)

def create_file(name,dic):
    """
    Funcion para crear un archivo de texto.
    """
    fname = f'final-{name}.txt'
    file = open(fname,'at')
    for llave in dic:
        try:
            file.write(dic[llave]+'\n')
        except:
            print('Error al escribir en el archivo',name)
    file.close()

file = open('files-merged.txt','rt')
dic_documentos = dict()
content = file.read().lower()
paragraph = content.split('\n')
#print(paragraph[:100])
i = 1
for linea in paragraph[:20]:
    dic_documentos[i]=paragraph[i-1]
    i+=1

#print(dic_documentos)
#print(dic_documentos.items)
#print('len: ',len(dic_documentos))


paragraph = delete_stopwords(dic_documentos)
#truncamiento(paragraph)
#lematizacion(paragraph)