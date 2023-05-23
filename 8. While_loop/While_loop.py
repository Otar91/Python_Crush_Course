current_number=1
while current_number<=10:
    print(current_number)
    current_number += 1

#Letting the user choose when to quit
#en estas primeras dos lineas se settea el mensaje inicial
prompt = '\nTell me somenting, and I will repeat it back you:\n'
prompt += "Enter 'quit' to end the program.\t"
#Python necesita comparar message con quit la primera vez por eso
#se guarda como basio para que python ejecute el ciclo inicial
message = ''
while message != 'quit':
    message = input(prompt)
    #pARA EVITAR   que cuando se ingresa quit se imprima
    if message != 'quit':
        print(message)


