mi_diccionario = {'nombre': 'bry', 'email': 'bry@mi.com', 'telefono': 3046702708}

mi_informacion = {
    'nombre': 'bry',
    'email': 'bry@mi.com',
    'telefono': 3046702708,
    'mascota': 'Zeus',
    'numero': [5]
}
print(mi_diccionario['nombre'])
print(mi_diccionario.get('mascota', 'N/A'))
print(mi_diccionario.get('nombre'))
print(mi_informacion['mascota'])
print(mi_informacion.get('apellido', 'N/A'))
print(mi_informacion.get('email'))

#############################################################################
 
contadores={}
alfabeto="abcdefghijklmnopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(3):
    cadena=input('Cadena de caracteres: ')
    for caracter in cadena:
        if caracter.lower() in alfabeto:
            contadores[caracter]+=1
for caracter,cantidad in contadores.items():
    print(caracter, ":",cantidad) 

###################################################

diccionario = {'Nombre': 'brayan', 'Edad': 28, 'Cursos': ['Curso 1', 'Curso 2', 'Curso 3']}

diccionario['Nombre']
print(diccionario.get('Nombre'))
diccionario['Saludos'] = 'Hola'     #Para agregar al diccionario
print(diccionario)
for key in diccionario:             #Para recorrer el diccionario
    print(diccionario[key])

dic = dict(nombre='brayan', edad=28)   #funcion dict para crear diccionario
print(dic)

print(diccionario.keys())
print(diccionario.values()) 

for key,value in diccionario.items():
    print(key, value) 

#####################################################################################

diccionario = {'a': 5, 6: True, (8,9):'str', 56: False} #Las claves deben ser inmutables 
print(diccionario)
diccionario['c'] = 10  #Agregar al diccionario 
diccionario['d'] = 20  #Si la llave/clave se encuentra actualiza si no crea 

valor = diccionario.get('a', (12,5))
del diccionario['a']    #del nos ayuda a eliminar la clave/llave

llaves = list(diccionario.keys())  #Objeto iterables
valores = list(diccionario.values())

llaves = tuple(diccionario.keys())
valores = tuple(diccionario.values())

diccionario_2 = {'g': 10, 25:'bry'}

diccionario_2.update(diccionario) #.upadate incrementa el diccionario 







        









