# Estas clases proporcionan funcionalidades para abrir, mejorar y filtrar imágenes, respectivamente.
from PIL import Image, ImageEnhance, ImageFilter
# que proporciona funciones para interactuar con el sistema operativo. Será utilizado para manejar los archivos en el directorio.
import os

#que representa la ruta del directorio donde se encuentran las imágenes que se desean editar
path = './imgs'
#La variable pathOut se establece en /editedImgs, que representa la ruta del directorio donde se guardarán las imágenes editadas
pathOut = '/editedImgs'

#se utiliza un bucle for en conjunto con os.listdir(path) para iterar sobre los archivos dentro del directorio especificado por path. 
# os.listdir() devuelve una lista de nombres de archivos y directorios en el directorio especificado.
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

#En esta línea, se aplica un filtro de nitidez (sharpen) a la imagen abierta


    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)


    factor = 1.5
    
    enhancer = ImageEnhance.Contrast(edit)

    edit = enhancer.enhance(factor)

#quí se obtiene el nombre base del archivo sin la extensión. 
# Se selecciona el primer elemento de la tupla, que corresponde al nombre del archivo sin la extensión.

    clean_name = os.path.splitext(filename)[0]

#En esta línea, se guarda la imagen editada (edit) en el directorio especificado por pathOut, 
# con un nuevo nombre que incluye el nombre base del archivo original seguido de "_edited"

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
