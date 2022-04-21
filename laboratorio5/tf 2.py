"""
En este programa se obtiene el tf de los documentos procesados en el laboratorio 4
"""
import pandas as pd
import numpy as np

def tf(documento):
    """
    Funcion para calcular la frecuencia apartir de un rango > de los documentos.
    Recibe como parametros:
    - documento (string)
    - min_frec (int)
    """
    dic_frecuencias = dict()
    INVALID=['0','1','2','3','4','5','6','7','8','9','',' ']
    
    paragraph = documento.split(' ')
    total_words = 0
    m=0
    for word in paragraph:
        if(len(word)>0): #Comprobamos si la palabra no es vacia
            if word[0] not in INVALID:
                total_words+=1
                if word in dic_frecuencias:
                    dic_frecuencias[word] += 1
                else:
                    dic_frecuencias[word] = 1
                    m=1+m
    #print('Total de palabras en el doc. =',total_words)
    
    dic_tf = dict()
    for llave in dic_frecuencias:
        dic_tf[llave]= round(dic_frecuencias[llave]/m,4)
        
    #print(dic_tf)
    return dic_tf

def vocuabulario(dic_documentos):
    dic_vocabulario = dict()
    
    for llave in dic_documentos:
        documento = dic_documentos[llave]

        frec_vocabulario = tf(documento)
        if(len(frec_vocabulario)>0):
            dic_vocabulario[llave] = frec_vocabulario
        
    print('>>>Calculando TF')
    return dic_vocabulario

def file_dict(name,dic):
    """
    Funcion para crear un archivo de texto a partir de un diccionario.
    Recibe como parametros:
    - name (string)
    - dic (diccionario)
    """
    fname = f'tf-{name}.csv'
    file = open(fname,'at')
    file.write('Documento,Palabra,Frecuencia\n')
    for llave in dic:
        frec = dic[llave]
        for llave2 in frec:
            parrafo = f'Doc {llave},{llave2},{frec[llave2]}\n'
            try:
                file.write(parrafo)
            except:
                print('Error al escribir en el archivo',name)
    file.close()


file_trunc = open('vocabulario total-truncamiento.csv','rt')
content_trunc = file_trunc.read().lower()

term_list = content_trunc.split('\n')
del(term_list[0])

#terminos
dic_documentos_trunc = dict()
file_trunc = open('documentos_prepro.txt','rt')
content_trunc = file_trunc.read().lower()

paragraph_trunc = content_trunc.split('\n')
i = 1
for linea in paragraph_trunc:
    dic_documentos_trunc[i]=paragraph_trunc[i-1]
    i+=1


#Generamos la matriz en el dataframe
documentos = len(dic_documentos_trunc.keys())
terminos = len(term_list)
matrix = np.zeros((documentos,terminos))

df = pd.DataFrame(matrix,index=dic_documentos_trunc.keys(),columns=term_list)
dic_doc = vocuabulario(dic_documentos_trunc)

i=0
for documento in dic_doc:
    for termino in dic_doc[documento]:
        
        j=0
        for t in term_list:
            if termino == t:
                df.iloc[i,j] = dic_doc[documento][termino]
                break
            j+=1
    i+=1

#Generamos la matriz de valores tf
df.to_csv('mtrx_tf.csv')