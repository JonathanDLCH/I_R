file = open('TRUNCAMIENT.txt','rt')
texto = file.read()

doc=open("longVocabulary1.txt",'w')
doc1=open("vocabulario1.txt",'w')

# Los caracteres que no contamos como palabras
quitar = ",;:.\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter, "")  # Remplazarlo por "nada"; es decir, removerlo
# Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
texto = texto.lower()
# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = texto.split(" ")
# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
diccionario_frecuencias1 = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1

    else:
        diccionario_frecuencias[palabra] = 1
print('Longitud original:',len(diccionario_frecuencias))
doc.write('\nLongitud del vocabulario original \n')
doc.write(str(len(diccionario_frecuencias)))

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")

    if diccionario_frecuencias[palabra] > 5 :
        print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
        diccionario_frecuencias1[palabra] = diccionario_frecuencias[palabra]

        doc1.write(palabra+'\n')

print('Longitud nueva:',len(diccionario_frecuencias1))
doc.write('\nLongitud del vocabulario sin frecuencia menor a 5 \n')
doc.write(str(len(diccionario_frecuencias1)))
