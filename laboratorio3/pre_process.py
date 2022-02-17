"""
Laboratorio 3
Generar ficheros:
-Consultas
-Documentos
"""
def open_files(*args):
    """
    Función para abrir los archivos que seran procesados,
    en caso de que no exista el archivo lo notificara pero no finalizara.
    *args -> Archivos a los que se les dará formato
    """
    for item in args:
        try:
            file = open(item,'rt')
            texto = file.read()
            print('Open >>>',item)
            formato(item,texto)
            file.close()
        except:
            print('Ocurrió un error al abrir el archivo',item)


def formato(item,texto):
    """
    Función para dar formato a los archivos de LISA
    Formato:
        <num> | <text>
        <num2> | <text2>
    """
    numeros=['0','1','2','3','4','5','6','7','8','9']
    limitadores=['#','*']
    #generamos nuestro nuevo archivo
    item = item.replace('docs','').replace('/','')
    fname = f'docs/format-{item}'
    new_file = open(fname,'at')
    #procesamos el contenido
    new_cadena=''
    for e in texto:
        if e in limitadores and new_cadena!='': #Si tiene un delimitador escribe la linea
            new_cadena=new_cadena+'\n'
            new_file.write(new_cadena)
            new_cadena=''
        elif e!='\n' and e not in limitadores:
            if new_cadena[-1:] in numeros and e not in numeros: #Numeró seguido de letra
                new_cadena=new_cadena+'| '+e 
            elif len(new_cadena)==0 and e not in numeros: #Si hay letras antes de un numeró
                continue
            else:
                new_cadena=new_cadena+e
        elif e=='\n' and new_cadena!='' and new_cadena[-1:] not in numeros:
            e=' '
            new_cadena=new_cadena+e


    new_file.close()

def merge_files(*args):
    """
    Funcion para unir varios documentos en uno solo.
    Nota: deben tener un formato correcto.
    """
    file_merge = open('files-merged.txt','at')
    for item in args:
        try:
            file = open(item,'rt')
            texto = file.read()
            file_merge.write(texto) 
            file.close()
        except:
            print('Error al abrir el archivo',item)
    file_merge.close()

open_files('docs/LISA.QUE','docs/LISA0.001','docs/LISA0.501','docs/LISA1.001','docs/LISA1.501','docs/LISA2.001','docs/LISA2.501','docs/LISA3.001','docs/LISA3.501','docs/LISA4.001','docs/LISA4.501','docs/LISA5.001','docs/LISA5.501','docs/LISA5.627','docs/LISA5.850')
merge_files('docs/format-LISA0.001','docs/format-LISA0.501','docs/format-LISA1.001','docs/format-LISA1.501','docs/format-LISA2.001','docs/format-LISA2.501','docs/format-LISA3.001','docs/format-LISA3.501','docs/format-LISA4.001','docs/format-LISA4.501','docs/format-LISA5.001','docs/format-LISA5.501','docs/format-LISA5.627','docs/format-LISA5.850')