# LIBRERIA PARA IMAGENES
from ntpath import join
from PIL import Image

#LIBRERIA PARA TEXTOS
import cv2

# REMOVER ARCHIVOS 
from os import remove
from cv2 import getTextSize

# PARA LECTURA DE IMAGENES HTTP
import requests as req
from io import BytesIO


# VARIABLES

# EQUIPO IZQUIERDA
logoIzq = 'https://cdn.api.everysport.com/logos/fotboll/olimpia_190518/1641998342298.png'
gols_one = "8"


# DATOS DE TABLA
equipoIzq = [
    "40%", 
    "7", 
    "9", 
    "8", 
    "5"
]

# EQUIPO DERECHA
logoDer = 'https://cdn.api.everysport.com/logos/fotboll/atletico_club_goianense_158404/1654764046179.png'
gols_two = "8"


# DATOS DE TABLA
equipoDer = [
    "60%", 
    "2", 
    "1", 
    "4", 
    "3"
]


# REQUEST DE LOGO CENTRAL ( LIGA )
try:                    
    response = req.get('https://res.cloudinary.com/dkrmpxrnl/image/upload/v1653753172/laliga_dcastl.png')
    LOGO = Image.open(BytesIO(response.content))
    LOGO.thumbnail((150,150))   
    LOGO.save('assets/laliga.png')

except:
    LOGO = Image.open('assets/balon.png')
    LOGO.save('assets/laliga.png')


# REQUEST DE LOGO EQUIPO IZQUIERDO 
try:
    response = req.get(logoIzq)
    LOGO = Image.open(BytesIO(response.content))
    LOGO.thumbnail((150,150))
    LOGO.save('assets/logopsg.png')

except:
    LOGO = Image.open('assets/balon.png')
    LOGO.save('assets/logopsg.png')


# REQUEST DE LOGO EQUIPO DERECHO 
try:
    response = req.get(logoDer)
    LOGO = Image.open(BytesIO(response.content))
    LOGO.thumbnail((150,150))
    LOGO.save('assets/logo-barcelona.png')

except:
    LOGO = Image.open('assets/balon.png')
    LOGO.save('assets/logo-barcelona.png')    


#LOGOS

# ABRE IMAGEN PLANTILLA EN BLANCO
img1 = Image.open('assets/img-white.jpg')

# ABRE LOGOS
logo1 = Image.open('assets/logopsg.png')
logo2 = Image.open('assets/logo-barcelona.png')
logo3 = Image.open('assets/laliga.png')

# RESIZE DE LOGOS
logo1.thumbnail((150,150))
logo2.thumbnail((150,150))
logo3.thumbnail((80,80))


img1_copy = img1.copy()

# MASCARA PARA TRASPARENCIA DE LOGOS

# LOGO CENTRAL
img1_copy.paste(logo3, (468,10), logo3)

# LOGO IZQUIERDO ( PSG PRUEBA )
img1_copy.paste(logo1, (145,50), logo1)

#LOGO DERECHO ( BACELONA )
img1_copy.paste(logo2, (727,50), logo2)


# GUARDAR IMAGEN TEMPORAL CON LOGOS
img1_copy.save('assets/img_logos.jpg')


# FUNCION PARA CALCULA EL CENTRO POR EL TAMAÑO DEL STRING
def calcularCentro(cadena, pos):
    countLetterI = 0
    calc = len(cadena) * 18 / 2
    posIzq = pos - round(calc)
    countLetterI = (cadena.count('I'))
    return posIzq + (countLetterI*8)


# TEXTOS
img = cv2.imread('assets/img_logos.jpg')

# GOLES EQUIPO IZQUERDA
position = (412,258)

# GOLES EQUIPO DERECHA

position2 = (552,258)


# CONFIG. DE FUENTE DE GENERALES DE FUENTES DE NUMERO DE GOLES
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 2
fontColor = (0,0,0)
fontWeight = 2


# ESCRIBE GOLES EQUIPO IZQUERDA
cv2.putText(img, gols_one, (calcularCentro(gols_one, 420),258), font, fontSize, fontColor, fontWeight, cv2.LINE_AA, False)

# ESCRIBE GOLES EQUIPO DERECHA
cv2.putText(img, gols_two,(calcularCentro(gols_two, 560),258), font, fontSize, fontColor, fontWeight, cv2.LINE_AA, False) 


# CONFIG. DE NOMBRE DE LOS EQUIPOS

nameTeamIzq = ("fc football").upper().split()
nameTeamDer = ("Atletiico Club Goianense").upper().split()



    
sizeTeamDer = len(nameTeamDer)
sizeTeamIzq = len(nameTeamIzq)


fontNameTeam = cv2.FONT_HERSHEY_SIMPLEX
fontSizeTeam = 1
fontColorTeam = (0,0,0)
fontWeightTeam = 2


# ESCRIBE NOMBRE DE EQUIPO IZQUERDA
if sizeTeamIzq == 1:
    cv2.putText(img, (nameTeamIzq[0]), (calcularCentro(nameTeamIzq[0], 205),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
if sizeTeamIzq == 2:
    cv2.putText(img, (nameTeamIzq[0]), (calcularCentro(nameTeamIzq[0], 205),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, (nameTeamIzq[1]), (calcularCentro(nameTeamIzq[1], 205),265), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
if sizeTeamIzq >= 3:
    cv2.putText(img, (nameTeamIzq[0]), (calcularCentro(nameTeamIzq[0], 205),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, (nameTeamIzq[1]), (calcularCentro(nameTeamIzq[1], 205),265), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, (nameTeamIzq[2]), (calcularCentro(nameTeamIzq[2], 205),295), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)

# ESCrIBE NOMBRE DE EQUIPO DERECHA



# ESCRIBE NOMBRE DE EQUIPO IZQUERDA
if sizeTeamDer == 1:
    cv2.putText(img, nameTeamDer[0], (calcularCentro(nameTeamDer[0], 765),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
if sizeTeamDer == 2:
    cv2.putText(img, nameTeamDer[0], (calcularCentro(nameTeamDer[0], 765),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, nameTeamDer[1], (calcularCentro(nameTeamDer[1], 765),265), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
if sizeTeamDer >= 3:
    cv2.putText(img, nameTeamDer[0], (calcularCentro(nameTeamDer[0], 765),232), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, nameTeamDer[1], (calcularCentro(nameTeamDer[1], 765),265), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)
    cv2.putText(img, nameTeamDer[2], (calcularCentro(nameTeamDer[2], 765),295), fontNameTeam, fontSizeTeam, fontColorTeam, fontWeightTeam, cv2.LINE_AA, False)


# CONFIG. DE FUENTE DE DATOS DE TABLA DE ESTADISTICAS

fontTable = cv2.FONT_HERSHEY_SIMPLEX
fontSizeTable = 1
fontColorTable = (0,0,0)
fontWeightTable = 1



# posIzq = 775 - round(calc)
# posDer = 775 - round(calc)

positionTableIzq = (215,365)
positionTableDer = (770,365)


# ESCIBE DATOS DE TABLA DE ESTADISTICAS

# EQUIPO IZQUERDA
for i in range(len(equipoIzq)):
        calc = len(equipoIzq[i]) * 18 / 2
        posIzq = positionTableIzq[0] - round(calc)
       
        cv2.putText(img, equipoIzq[i], (posIzq, positionTableIzq[1] + i*50), fontTable, fontSizeTable, fontColorTable, fontWeightTable, cv2.LINE_AA, False)

# EQUIPO DERECHA
for i in range(len(equipoDer)):
    calc = len(equipoDer[i]) * 18 / 2
    posDer = positionTableDer[0] - round(calc)
    cv2.putText(img, equipoDer[i], (posDer, positionTableDer[1] + i*50), fontTable, fontSizeTable, fontColorTable, fontWeightTable, cv2.LINE_AA, False)


# GUARDAR IMAGEN GENERADA CON TEXTOS
cv2.imwrite('img_generated.jpg', img)

# BORRA IMAGEN TEMPORAL DONDE SE COPIAN LOS LOGOS
remove('assets/img_logos.jpg')

# BORRA LOGOS QUE SE GUARDAN EN LA PETICION HTTP Y SE INCLUYERON EN LA IMAGEN
remove('assets/laliga.png')
remove('assets/logopsg.png')
remove('assets/logo-barcelona.png')

cv2.imshow('img_generated',img)
cv2.waitKey()

