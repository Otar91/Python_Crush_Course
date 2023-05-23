#7.4 LOOPS WHILE
prompt = '\nHello, Wicht toppings do you like to agree on your pizza?\n'
prompt += 'Please write what toppings you what to agree on your pizza\n'
prompt += "Write 'quit to finish\n"


flagg = 1
while flagg != 0:
    data = input(prompt)
    if data == 'quit':
        flagg = 0
    else:
        print('\nWe are adding ' + data.title() + ' on your pizza\n')

