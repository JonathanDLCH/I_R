"""
Aplicando truncamiento y lematizacion con nltk
"""
from nltk.corpus import stopwords

def delete_stopwords(paragraphs):
    """
    Funcion que nos permite estructurar el texto,
    quitamos simbolos y palabras vacias.
    """
    words=[line.split() for line in paragraphs[:10]]
    print(words)
    print(type(words))
    



file = open('files-merged.txt','rt')
content = file.read().lower()
paragraph = content.split('\n')

print(paragraph[:5])
delete_stopwords(paragraph)
