print('-----------------')
print('| informe de calificaciones |')

alumno=(input('\nNombre del alumno: '))

n1=float(input('Ingrese nota1: '))
n2=float(input('Ingrese nota2: '))
n3=float(input('Ingrese nota3: '))

promedio=(n1+n2+n3)/4

if promedio > 3:
    print('Aprobo', promedio)
elif promedio ==3:
    print('Aprobo', promedio)
else:
    print('reprobado', promedio)

###############################################

alumno=(input('\nNombre del alumno: '))
n=float(input('\nNumeros de notas: '))
suma=0
i=1
while (i<=n):
    print('\nIngrese nota: ', i)
    nota=float(input())
    suma=suma+nota
    i+=1
    promedio=suma/n
if promedio >=3.0:
    print('\nAprobo', promedio)
else:
    print('\nReprobo', promedio)
