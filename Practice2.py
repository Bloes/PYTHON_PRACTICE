print('----------')
precioProd1=float(input('Digite el producto 1: '))
precioProd2=float(input('Digite el producto 2: '))

print('----------')
print('Inicia if precioprod1 > precioprod2 ')
if precioProd1 > precioProd2:
    print('\nEl precioprod1 es mayor al precioprod2\n')
elif precioProd1 == precioProd2:
    print('\nEl precioprod1 es igual al precioprod2\n')
else:
    print('\nEl precioprod1 es menor al precioprod2\n')

print('--------------------')
###############################################################
numero=int(input('Digite un número: '))

divEnt=int(numero/2)
comprobar=divEnt*2

if numero == comprobar:
    print('La respuesta es True')
    print('\nEl número', numero, 'es Par\n')
else:
    print('La respuesta es False')
    print('\nEl número', numero,'es Impar\n')