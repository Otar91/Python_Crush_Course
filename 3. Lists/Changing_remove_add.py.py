#Changing, adding and removing elements

#1.Modifying elements in a list\
motorcycles=['Honda','susuki','yamaha']
print(motorcycles);
motorcycles[0]='AKT';
print(motorcycles);

#append elements in the end of a list
motorcycles=['Honda','susuki','yamaha'];
print(motorcycles);
motorcycles.append('Ducati');
print(motorcycles);

#Insert elements in any position in a list
motorcycles=['Honda','susuki','yamaha'];
print(motorcycles);
motorcycles.insert(1,'AKT'); #No reemplaza el elemento en la posicion sino que hace espacio moviendo todo el resto de elementos a la derecha
print(motorcycles); 

#Removing elements from a list using 'del' statement
motorcycles=['AKT','Honda','Ducaty'];
print(motorcycles);
del motorcycles[0]; #Del statement for delete elements in a list
#la instruccion 'Del', no permite trabajar con los elementos eliminados
print(motorcycles);

#Removing elements using pop() method
motorcycles=['honda','yamaha','suzuki'];
print(motorcycles);
popped_motorcycles=motorcycles.pop();   #El metodo pop elimina el ultimo elemento de una lista
print(motorcycles);
print(popped_motorcycles);

#ejemplo sobre la utilidad del metodo pop()
motorcycles=['AKT','suzuki','honda'];
print('La ultima motocicleta comprada fue '+motorcycles.pop().title()+ ' en 2020');

#Popping items from any position in a list
first_owend=motorcycles.pop(0);
print('La motocicleta mas barata que compre es la '+ first_owend.title());

#Removing item from a list by value
#el metodo remove permite eliminar elementos de una lista conociendo no su posicion sino su valor
motorcycles=['AKT','Ducaty','Honda','Yamaha']
print(motorcycles);
motorcycles.remove('Ducaty');
print(motorcycles);

#Ejemplo de uso de remove
motorcycles=['AKT','Ducaty','Honda','Yamaha']
print(motorcycles);
too_expensive='Ducaty';
motorcycles.remove(too_expensive);
print(motorcycles);
print('\nA '+too_expensive.title()+ ' is too expensive for me');
