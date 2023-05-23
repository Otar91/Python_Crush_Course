message=input('Tellme something and I will repeat it back to you: ')
print(message)

#=================================================================================
prompt = 'If you tell us who are you, we can personalize the messages you see'
prompt += '\nWhat is your first name?\n'
#Esta es una forma de crear un input con multiples lineas de texto.
name = input(prompt)
print('\nHello, '+name.title()+'.')

#Conver a str in a integer with int() function 
age = input('How old are you?\n')
age=int(age)#input registra la informacion ingresada con un string hay que convertirla a integer 
if age>=21:
    print('True')

