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