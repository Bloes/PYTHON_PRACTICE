#variableDefinida=int()
#variableDefinida=10
#precEntrMuseo="Error al seleccionar ...."
#edad=6
edad=int(input('\nDigite la edad del visitante Museo: '))

if edad < 12:
    precEntrMuseo=10000
elif edad < 18:
    precEntrMuseo=20000
elif edad < 60: 
    precEntrMuseo=60000
else: 
    precEntrMuseo=30000

print('\nEl costo de la entrada del museo es: ',precEntrMuseo)
print('----------------------------------------------------------')

fds=input('\nEs fin de semana o festivo (S/N)\n')
if fds == "S" or fds == "s":
    fds = True
else:
    fds = False

edad=int(input('\nDigite edad: '))
estatura=float(input('Digite estatura: '))

if edad < 12:
    precEntrMuseo = 10000
elif edad < 18:
    precEntrMuseo = 20000
elif edad < 60:
    precEntrMuseo = 60000
else:
    precEntrMuseo = 30000

if fds:
    precEntrMuseo += 3000
if fds:
    precEntrMuseo *= 1.30


print('\nEl costo de la entrada del museo es: ',precEntrMuseo, '\n')