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
    print('StopWords...')
    for llave in dic_documentos:
        documento = dic_documentos[llave]
        re_punc = re.compile('[%s]'%re.escape(string.punctuation))
        documentoaux=""
        for word in documento:
            if word in re_punc.sub('',word):
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

def truncamiento(dic_documentos):
    """
    Funcion para truncar palabras con el algoritmo de PorterStemmer
    """
    print('\nPorterStemmer...')
    porter = PorterStemmer()
    for llave in dic_documentos:
        words=""
        documento = dic_documentos[llave]
        documentoaux=documento.split(' ')
        for word in documentoaux:
            words+=' '+porter.stem(word)
        dic_documentos[llave] = words

    create_file('truncamiento',dic_documentos)

def lematizacion(dic_documentos):
    """
    Funcion para lematizar nuestro contenido
    """
    print('\nWordNetLemmatizer...')
    wnl = WordNetLemmatizer()
    for llave in dic_documentos:
        words=""
        documento = dic_documentos[llave]
        documentoaux=documento.split(' ')
        for word in documentoaux:
            words+=' '+wnl.lemmatize(word)
        dic_documentos[llave] = words
    create_file('lematizacion',dic_documentos)

def create_file(name,dic):
    """
    Funcion para crear un archivo de texto a partir de un diccionario.
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
i = 1
for linea in paragraph:
    dic_documentos[i]=paragraph[i-1]
    i+=1

delete_stopwords(dic_documentos)
truncamiento(dic_documentos)
lematizacion(dic_documentos)