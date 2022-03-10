"""
En este programa se obtiene el vocabulario de los documentos procesados en el laboratorio3
"""

def frecuencia(documento,min_frec):
    dic_frecuencias = dict()
    INVALID=['0','1','2','3','4','5','6','7','8','9','',' ']
    
    paragraph = documento.split(' ')
    for word in paragraph:
        if(len(word)>0): #Comprobamos si la palabra no es vacia
            if word[0] not in INVALID:
                if word in dic_frecuencias:
                    dic_frecuencias[word] += 1
                else:
                    dic_frecuencias[word] = 1

    valores = dic_frecuencias.values()
    dic_frecuencias_final = dict()
    for llave in dic_frecuencias:
        if(dic_frecuencias[llave] >= min_frec):
            dic_frecuencias_final[llave]= dic_frecuencias[llave]

    #print(dic_frecuencias_final)
    return dic_frecuencias_final


def vocabulario_total(dic_documentos):
    INVALID=['0','1','2','3','4','5','6','7','8','9','',' ']
    vocabulario = list()
    print('>>>Calculando vocabulario total')
    for llave in dic_documentos:
        documento = dic_documentos[llave]
        paragraph = documento.split(' ')

        for word in paragraph:
            if(len(word)>0): #Comprobamos si la palabra no es vacia
                if word[0] not in INVALID and word not in vocabulario:
                    vocabulario.append(word)
    
    #print(vocabulario)
    return vocabulario

def vocuabulario(dic_documentos):
    min_frec = 5
    dic_vocabulario = dict()
    
    for llave in dic_documentos:
        documento = dic_documentos[llave]

        frec_vocabulario = frecuencia(documento,min_frec)
        if(len(frec_vocabulario)>0):
            dic_vocabulario[llave] = frec_vocabulario
        
    print('>>>Vocabulario')
    #print(dic_vocabulario)
    return dic_vocabulario

def file_List(name,list):
    """
    Funcion para crear un archivo de texto a partir de un diccionario.
    """
    fname = f'vocabulario total-{name}.csv'
    file = open(fname,'at')
    file.write('Palabra\n')
    for e in list:
        try:
            file.write(e+'\n')
        except:
            print('Error al escribir en el archivo',name)
    file.close()

def file_dict(name,dic):
    """
    Funcion para crear un archivo de texto a partir de un diccionario.
    """
    fname = f'vocabulario-{name}.csv'
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


dic_documentos_trunc = dict()
dic_documentos_lem = dict()
file_trunc = open('final-truncamiento.txt','rt')
file_lem = open('final-lematizacion.txt','rt')
content_trunc = file_trunc.read().lower()
content_lem = file_lem.read().lower()

paragraph_trunc = content_trunc.split('\n')
i = 1
for linea in paragraph_trunc:
    dic_documentos_trunc[i]=paragraph_trunc[i-1]
    i+=1

paragraph_lem = content_lem.split('\n')
i = 1
for linea in paragraph_lem:
    dic_documentos_lem[i]=paragraph_lem[i-1]
    i+=1


voc_trun = vocabulario_total(dic_documentos_trunc)
file_List('truncamiento',voc_trun)
voc_lem = vocabulario_total(dic_documentos_lem)
file_List('lematizacion',voc_lem)

voc_fre5_trunc = vocuabulario(dic_documentos_trunc)
print('salida1:',type(voc_fre5_trunc))
file_dict('frec5_truncamiento',voc_fre5_trunc)
#voc_frec5_trunc_words = vocabulario_total(voc_fre5_trunc)
#file_List('truncamiento-frec5Voc',voc_frec5_trunc_words)

voc_fre5_lem = vocuabulario(dic_documentos_lem)
print('salida1:',type(voc_fre5_trunc))
file_dict('frec5_lematizacion',voc_fre5_lem)
#voc_frec5_lem_words = vocabulario_total(voc_fre5_lem)
#file_List('lematizacion-frec5Voc',voc_frec5_lem_words)