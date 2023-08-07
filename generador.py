import os
os.system('cls')

from diccionario import *


def opcionMultiple(text, opciones = ['s', 'n'], siError ='Solo "s" y "n" son opciones válidas') :
  while True:
    opcion = str(input(text).strip())
    if opcion.lower() not in opciones:
      print(siError)
    else:
      break
  return (opcion)
#
def elegirIdioma():
  for key in textos:
    print(textos[key]['elegir'])
  
  lan = opcionMultiple('->\033[32m ',opcionesValidas['elegir'],opcionesValidas['error'])
  idioma = idiomaElegido[lan]
  return idioma
# 
def crearPW(numero, extension):
  print(extension)
#

idioma = elegirIdioma()
print(textos[idioma]['cantidad caracteres'])
try:
  extension = int(input('->\033[32m '))
except:
  extension = 8
print('\033[0m')

crearPW(1,extension)
