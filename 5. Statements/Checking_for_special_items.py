#Checking for special items
requested_toppins=['mushrooms','green peppers','extra cheese']

for requested_toppin in requested_toppins:
    if requested_toppin=='green peppers':
        print('Sorry we are out of green peppers right now')
    else:
        print('Adding '+ requested_toppin + '.')
print('\nFinished making your pizza!')


#Work with empty lists
requested_toppins=[]
#La lista esta vacia, luego se aplica un 'if' que anida un for que se mueve por todos los elementos
#de la lista y los va imprimiendo, pero si no se cumple esta condicion por que la lista esta vacia
#se imprime un mensaje de confirmacion de que el cliente quiere una piza sencilla
if requested_toppins:
#Cuando el nombre de una lista es usado en un 'if' statement Python regresa True si la lista contiene
#al menos un elemento
    for requested_toppin in requested_toppins:
        print('Adding '+requested_toppin+'.');
    print('\nFinished making your pizza');
else:
    print('Are you sure you want to plain pizza?');

#Using multiple lists
available_toppins=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppins=['mushrooms','french fries','extra cheese']

for requested_toppin in requested_toppins:
    if requested_toppin in available_toppins:
        print('Adding '+requested_toppin)
    else:
        print('Sorry, we dont have '+requested_toppin)
print('\nFinished making your pizza')