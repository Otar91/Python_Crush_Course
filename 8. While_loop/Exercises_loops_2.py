#precies of movie tickets

#v1 Use a conditional test in the while statement to stop the loop
prompt = "Hi, we have 3 prices' categories in function of your age, "
prompt += 'then, how old you are?\n'
data=input(prompt)
flagg = 0
while flagg == 0:
    age=int(data)
    if age < 3:
        print('You tick is free')
        flagg = 1
    elif age <= 12:
        print('You tick costs $10')
        flagg = 1
    else:
        print('You tick costs $15')
        flagg = 1


#v2 Use a vreak statement
prompt = "Hi, we have 3 prices' categories in function of your age, "
prompt += 'then, how old you are?\n'
prompt += 'If you want to exit write quit\n'
while data != 'quit':
    data=input(prompt)
    age=int(data)
    if age < 3:
        print('You tick is free')
    elif age <= 12:
        print('You tick costs $10')
    else:
        print('You tick costs $15')
    