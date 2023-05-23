prompt = 'Please enter a name of a city that you are visited'
prompt += "\nEnter 'quit' when you are finished\n"

#I while loop that run with 'true'will run forever unlees it reaches a break statement
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love go to " + city.title() + '!')

#========================================================================================

#continue statement
#printing odd numbers with continue statement
current_number = 0
while current_number <= 10:
    current_number += 1
#Si el 'if' se cumple statement continue te devuelve al inicio del ciclo while y no ejecuta 
#el resto del codigo, sino se cumple sigue ejecutando el codigo en este caso el print()
    if current_number % 2 == 0:
        continue
    print(current_number)