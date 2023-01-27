x = list(range(2,20,2))
for i in x:
    print(i)   ##Me Crea nueve listas

#####################################3
y = list(range(2,0,-2))
for b in y:
    print(b)   ##Me Crea nueve listas
#####################################
my_list = [2,5]
my_list.append([10,5])
print(my_list)
####################################
my_list = [2, 5]
my_list.extend([10, 5])
print(my_list)
####################################
my_list = [2, 5]
my_list.pop()
print(my_list)
