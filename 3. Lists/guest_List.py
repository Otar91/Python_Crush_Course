guests=['Albert Eistein','Jenny Bautista','Euler'];
print(guests);
print('Hola '+guests[0]+' me gustaria invitarte a cenar.');
print('Hola '+guests[1]+' me gustaria invitarte a cenar.');
print('Hola '+guests[2]+' me gustaria invitarte a cenar.');
print(guests[2]+' no puede venir a cenar.')
#modify list
guests[2]='Samuel David';
print('Hola '+guests[2]+' me gustaria invitarte a cenar.');

#Add more guest by dinner
guests.append('Carlos Garcia');
guests.append('Doris Martinez');
guests.append('Diego Medina');

print('La lista de invitados se ha modificado, la nueva lista es:\n');
print(guests);

print('He tenido un contratiempo, solo puedo invitar dos personas a la cena');
print('Hola '+ guests.pop()+' lo siento ya no estas invitado a la cena');
print('Hola '+ guests.pop()+' lo siento ya no estas invitado a la cena');
print('Hola '+ guests.pop()+' lo siento ya no estas invitado a la cena');
print('Hola '+ guests.pop()+' lo siento ya no estas invitado a la cena');
print(guests);
del guests[-1];
del guests[-1];
print(guests);