value=0
it=0
while value < 10:
    if value > 5:
        value = value+2
    else:
        value=value+1
        it=it+1
print(it)
print('--------------------------')

items=[3,4,5]
for values in items:
    items=2*items
print(items)
print('---------------------------------------')

contador=2
bandera=False
while bandera:
    print('Contador va en ', contador)
    if contador == 3:
        bandera= False
        contador += 1 
print('Contador 1 termina en: ', contador)
print('Salio del while')
print('--------------------------------------')

contador=2
while contador < 3:
    contador +=1
print('Contador va en: ', contador)
print('-------------------------------------------------')

for i in range(4):
    print('\nVariable i: ', i, '\n')
print('\nTermina el for\n')

for i in range(2,4):
    print('\nVariable i: ', i, '\n')
print('\nTermina for\n')

for b in range(2,10+5,2):
    print('\nVariable b: ', b, '\n')
print('\nTermina el for\n')

for j in range(2,2-5,-6):
    print('\nVariable j: ', j, '\n')
print('\nTermina el for\n')
print('--------------------------------------------')

incia=0
termina=20
incremento=1

for i in range(incia,termina,incremento):
    print('\nVariable i: ', i, '\n')
print('\ni termina en: ', i, '\n')
print('\nTermina el for\n')
