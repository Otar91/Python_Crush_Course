#using a flag
flag = True #setteo de la bandera
prompt = '\nTell me somenting, and I will repeat it back you:\n'
prompt += "Enter 'quit' to end the program.\t"
while flag: #Mientras flagg siga siendo True
    message = input(prompt)
    if message == 'quit':
        flag=False #se over settea el valor de flag
    else:
        print(message)


