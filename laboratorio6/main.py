import math
import pandas as pd

def idf(total_Doc,terminos,docs_termino):
    idf_dic = dict()
    for termino in terminos:
        try:
            valor = math.log(total_Doc/docs_termino[termino])
            idf_dic[termino] = valor
        except:
            idf_dic[termino] = 0
            #print('no se encontro',termino)

    return idf_dic

def file_dict(name,dic):
    """
    Funcion para crear un archivo de texto a partir de un diccionario.
    Recibe como parametros:
    - name (string)
    - dic (diccionario)
    """
    fname = f'{name}.csv'
    file = open(fname,'at')
    file.write('Termino,IDF\n')
    for termino in dic:
        idf = dic[termino]
        parrafo = f'{termino},{idf}\n'
        try:
            file.write(parrafo)
        except:
            print('Error al escribir en el archivo',name)
            
    file.close()

#Lista de terminos

file_trunc = open('vocabulario total-truncamiento.csv','rt')
content_trunc = file_trunc.read().lower()

term_list = content_trunc.split('\n')
del(term_list[0])


#Abrir dicionario
dic_doc_voc = dict()
file_trunc = open('vocabulario-tf_truncamiento.csv','rt')
content_trunc = file_trunc.read().lower()

paragraph_trunc = content_trunc.split('\n')
#del paragraph_trunc[0]


i = 1
terminos = list()
for linea in paragraph_trunc:

    info = linea.split(',')
    n_doc = info[0].replace('doc ','')
    #print(linea)
    try:
        n_doc = int(n_doc)
    except:
        continue

    if n_doc == i :
        terminos.append(info[1])
    else:
        dic_doc_voc[n_doc-1] = terminos
        i+=1
        terminos = list()
        terminos.append(info[1])

#print(dic_doc_voc)

#Conteo
Nt = dict()
for termino in term_list:
    cnt=0
    for doc in dic_doc_voc:
        if termino in dic_doc_voc[doc]:
            dic_doc_voc[doc].remove(termino)
            cnt+=1
            #recorremos todo el diccionario para contar
    
    if cnt != 0:
        Nt[termino]= cnt


list_idf = idf(6000,term_list,Nt)
#file_dict('idf',list_idf)


#abrimos la matrix de tf
df=pd.read_csv('mtrx_tf.csv')
df.drop(['doc'],axis=1,inplace=True)

print(df)
dftotal=df*list_idf
print(dftotal['indian'])

#Guardamos la matrix tf-idf
dftotal.to_csv('tf-idf.csv')
