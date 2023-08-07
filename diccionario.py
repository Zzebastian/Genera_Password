
textos = {'Esp': {}, 'Eng': {}}

textos['Esp'] = {'elegir': '\033[0mElija el idioma de operación, solo se admiten español (\033[32m1\033[0m) e ingles (\033[32m2\033[0m).',
                 'error eleccion': '\033[0mSolo se pueden elegir \033[32m1\033[0m o \033[32m2\033[0m',
                 'agregar valor' : '\033[0mSi Desea agregar un elemento que modifique la contraseña \hágalo ahora, de lo contrario ingrese "Enter"',
                 'cantidad caracteres': '\033[0mIngrese la cantidad de caracteres que desea tener por contraseña, 8 por defecto',
                 }

textos['Eng'] = {"elegir": "\033[0mSelect the operating language, only Spanish (Esp) and English (Eng) are supported.\033[0m",
                 "error eleccion": "\033[0mOnly Esp or Eng can be selected.\033[0m",
                 
}
idiomaElegido = {'1': 'Esp', '2': 'Eng'}


opcionesValidas = {'Esp': {}, 'Eng': {}, 'elegir':['1', '2'], }

opcionesValidas['error'] = ''
for key in textos:
    opcionesValidas['error'] += textos[key]['error eleccion'] + '\n'


# opcionesValidas['Esp'] = {

# }

# import os
# os.system('cls')

# for key in textos['Esp']:
#     print(key, " / ", textos['Esp'][key])
# # "Only (y)es and (n)o are available options"