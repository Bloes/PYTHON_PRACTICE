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

