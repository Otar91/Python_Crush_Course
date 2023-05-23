for value in range(1,5):
    print(value) #The range() function empieza en el primer valor dado y se detiene un paso antes de alcanzar el segundo valor
                    #por eso en este ejemplo nunca imprimira el valor 5

#list() function
numbers=list(range(1,10));
print(numbers)

#skip numbers in a list with range() function
even_numbers=list(range(2,11,2)); #el ultimo argumento de la funcion le indica a range el paso de la generacion
print(even_numbers);

#Squares numbers 1 to 10
squares=[];
for value in range(1,11):
    square=value**2;
    squares.append(square);
print(squares);

#Other way more efficient to write the same code
squares2=[];
for value in range(1,11):
    squares2.append(value**2)
print(squares2);
