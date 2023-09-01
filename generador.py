import os
os.system('cls')

from diccionario import *
import random


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
def crearPW(extension):
  global idioma
  
  primosNecesarios = int((2*extension + 6)/ 5)+1
  generadorCaracteres = 1

  for i in range(0, primosNecesarios+1):
      generadorCaracteres *= random.choice(numerosPrimos)
  j = 0
  character = []
  password = ""
  gcStr = str(generadorCaracteres)
  for i in range(0,len(gcStr),2):
    elemento = int(gcStr[i:i+2])
    if elemento > 0 and elemento <= 93:
      character.append(elemento+33)
      password += chr(elemento+33)
      j += 1
      if j >= extension:
        break

  print("Contraseña = ", password)
  

  
idioma = elegirIdioma()
print(textos[idioma]['cantidad caracteres'])
try:
  extension = int(input('->\033[32m '))
except:
  extension = 8
print('\033[0m')
crearPW(extension)
