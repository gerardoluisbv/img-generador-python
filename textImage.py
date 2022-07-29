# LIBRERIA PARA IMAGENES
from PIL import Image

#LIBRERIA PARA TEXTOS
import cv2
import textwrap

# REMOVER ARCHIVOS 
from os import remove
from cv2 import getTextSize

# PARA LECTURA DE IMAGENES HTTP
import requests as req
from io import BytesIO

#MANEJO DE ARREGLOS
import numpy as np


################## FUNCIONES ###################

# ESCRIBE Y HACE WRAP DE LOS NOMBRES DE LOS EQUPOS DADO UN TEXTO Y COORDENADAS
def writeTeam (text,sizex,sizey):


    font = cv2.FONT_HERSHEY_SIMPLEX

    wrapped_text = textwrap.wrap(text, width=15)
    x, y = 10, 50
    font_size = 1
    font_thickness = 2

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 16

        y = int((sizex + textsize[1]) / 2) + i * gap
        x = int((sizey - textsize[0]) / 2)

        cv2.putText(img, line, (x, y), font,
                    font_size, 
                    (0,0,0), 
                    font_thickness, 
                    lineType = cv2.LINE_AA)


# ESCRIBE DATOS DE TABLA DE ESTADISTICAS
def writeDataTable(arrayData,position):
    for i in range(len(arrayData)):
        calc = len(arrayData[i]) * 18 / 2
        pos = position[0] - round(calc)
        cv2.putText(img, arrayData[i], (pos, position[1] + i*50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 1, cv2.LINE_AA, False)



# FUNCION PARA CALCULA EL CENTRO POR EL TAMAÑO DEL STRING
def calcularCentro(cadena, pos):
    countLetterI = 0
    calc = len(cadena) * 18 / 2
    posIzq = pos - round(calc)
    countLetterI = (cadena.count('I'))
    return posIzq + (countLetterI*8)



############################################### VARIABLES ###############################################


################# EQUIPO IZQUIERDA ################# 
logoIzq = 'https://cdn.api.everysport.com/logos/fotboll/olimpia_190518/1641998342298.png'

nameTeamIzq = ("equipo pc. de nombre largo").upper()

gols_one = "4"


# DATOS DE TABLA
equipoIzq = [
    "40%", 
    "7", 
    "9", 
    "8", 
    "5"
]


################# EQUIPO DERECHA ################# 
logoDer = 'https://cdn.api.everysport.com/logos/fotboll/atletico_club_goianense_158404/1654764046179.png'

nameTeamDer = ("nombre corto").upper()

gols_two = "2"


# DATOS DE TABLA
equipoDer = [
    "60%", 
    "2", 
    "1", 
    "4", 
    "3"
]


#FUNCION QUE HACE LA PETICION Y GUARDA LA IMAGEN
def requestImg(url,path):
    try:                    
        response = req.get(url)
        LOGO = Image.open(BytesIO(response.content))
        LOGO.thumbnail((150,150))   
        LOGO.save(path)

    except:
        LOGO = Image.open(path)
        LOGO.save(path)




################## LLAMADO DE FUNCIONES ###################     

logoliga = 'https://res.cloudinary.com/dkrmpxrnl/image/upload/v1653753172/laliga_dcastl.png'


# LLAMADO A LA FUNCION RECIBE EL URL Y EL PATH CON EL NOMBRE CON QUE SE GUARDARA EL ARCHIVO

requestImg(logoliga,'assets/laliga.png')  

requestImg(logoIzq,'assets/logoizq.png')

requestImg(logoDer,'assets/logoder.png')



#LOGOS

# ABRE IMAGEN PLANTILLA EN BLANCO
img1 = Image.open('assets/img-white.jpg')

# ABRE LOGOS
logo1 = Image.open('assets/logoizq.png')
logo2 = Image.open('assets/logoder.png')
logo3 = Image.open('assets/laliga.png')

# RESIZE DE LOGOS
logo1.thumbnail((150,150))
logo2.thumbnail((150,150))
logo3.thumbnail((80,80))


img1_copy = img1.copy()

# MASCARA PARA TRASPARENCIA DE LOGOS

# LOGO CENTRAL
img1_copy.paste(logo3, (460,10), logo3)

# LOGO IZQUIERDO ( PSG PRUEBA )
img1_copy.paste(logo1, (145,20), logo1)

#LOGO DERECHO ( BACELONA )
img1_copy.paste(logo2, (727,20), logo2)


# GUARDAR IMAGEN TEMPORAL CON LOGOS
img1_copy.save('assets/img_logos.jpg')


# TEXTOS
img = cv2.imread('assets/img_logos.jpg')


# ESCRIBE GOLES EQUIPO IZQUERDA
cv2.putText(img, gols_one, (calcularCentro(gols_one, 435),195), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2, cv2.LINE_AA, False)

# ESCRIBE GOLES EQUIPO DERECHA
cv2.putText(img, gols_two,(calcularCentro(gols_two, 545),195), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2, cv2.LINE_AA, False) 


# LLAMADO DE FUNCIONEN QUE ESCRIBE NOMBRE DE LOS EQUIPOS
writeTeam(nameTeamIzq,380,435)
writeTeam(nameTeamDer,380,1550)

# LLAMADO DE FUNCIONEN QUE ESCRIBE DATOS EN TABLE 
writeDataTable(equipoIzq, (215,326))
writeDataTable(equipoDer, (770,326))



# GUARDAR IMAGEN GENERADA CON TEXTOS
cv2.imwrite('img_generated.jpg', img)

# BORRA IMAGEN TEMPORAL DONDE SE COPIAN LOS LOGOS
remove('assets/img_logos.jpg')

# BORRA LOGOS QUE SE GUARDAN EN LA PETICION HTTP Y SE INCLUYERON EN LA IMAGEN
remove('assets/laliga.png')
remove('assets/logoizq.png')
remove('assets/logoder.png')

cv2.imshow('img_generated',img)
cv2.waitKey()

