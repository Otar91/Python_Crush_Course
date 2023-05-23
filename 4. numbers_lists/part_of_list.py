#Slicing a list
players=['Andres','Carlos','Diego','Alberto','Samuel','David'];
print(players[0:3]);#dentro del corchete se coloca el indice del primer elemento y del ultimo elementos separados por dos puntos
                    #el indice final es igual que con range, no se incluye a la hora de crear el slicing y los indices empiezan en cero
print(players[1:4]);
print(players[:3]); #Si se omite el primer indice Python automaticamente inicia el slice en el index 0
print(players[2:]);#similar si se omite el segundo indice Python empieza en el primer index dado hasta el final de la lista
print(players[-4:]);#con el signo negativo se usa para empezar a contar desde la posicion final de la lista

#======================foor througth slices in a list=========================================
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print('\nHere are the first three players at the list:');
for player in players[:3]:
    print(player.title());


#=========================Copying a list==============================================

my_foods=['pizza','falafel','carrot cake'];
friend_food=my_foods[:]; #Una opcion para crear una copia de una lista es dejar sin ingresar tanto el primer index como el segundo como si se estuviera creando un slice
friend_food.append('ice cream');
my_foods.append('canoli');
print(friend_food);
print(my_foods);




















