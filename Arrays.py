#Tenemos Listas

dato_x = [1,2,5,6]
dato_y = ['a','b','c','d']

#Tenemos Tuplas
tupla_x = (1,2,5,6)
tuplas_y= ('a','b','c','d')

print(dato_x[2])
print(dato_y[3])
print(tupla_x[2])
######################################

lista = [1,2.5,'devcode',[5,6],4]

print(lista[1:3])
print(lista[1:6])
print(lista[1:6:2])
print(lista[::-1])

for i in range(len(lista)):
    print(lista[i])
##########################################

lista = [1,2.5,'devcode',[5,6],4, [7,8]]
for element in lista:
    print(element)

###########################################
letras = ['a','b','c','d']
print(letras)
print(len(letras))
print(letras[0])
for i in range(len(letras)):
    print(letras[i])
letras.append('e')  #.append permite añadir un elemento 
print(letras)

letras.extend(['f','g','h'])  #.extend permite agregar elementos iterables
print(letras)
##############################################
letras = ['a','b','c','d']
numeros =[1,2,3]
letras.extend(numeros)  #.extend agregamos mas listas 
print(letras)

letras.insert(0,4)   #.insert permite añadir un elemento y posicion 
print(letras)

l = [5,6,8]
l.insert(2,9)
print(l)

l.pop(0)  #.pop quita un elemento de la lista 
print(l)

l.remove(8)  #.remove quita un elemento de la lista nombrandolo 
print(l) 





    
