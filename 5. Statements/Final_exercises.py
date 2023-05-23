usernames=['el gato volador','lopesto','tutaina','first_class','pepe','admin']
for username in usernames:
    if username == 'admin':
        print('Hello admin would you like to see a status report')
    else:
        print('Hello '+ username.title() + ' thank you for logging in again')

#No users
usernames=[]
if usernames:
    for username in usernames:
        print('Hello '+ username.title() + ' thank you for logging in again')
else:
    print('We need to find some users, quickly!!!')

#Checking usernames
current_users=['gato volador','lopesto','tutaina','first_class','pepe','admin']
new_users=['Gato volador','andrew','estrellita','nahibal','goleador']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, the username ' + new_user +' is not available, you need try again')
    else:
        print('The username ' + new_user + ' is available') 

#ordinal numbers
numbers=list(range(1,10))
aa=[1,2,3]
for number in numbers:
    if number in aa and number == 1:
        print(str(number)+'st')
    elif number in aa and number == 2:
        print(str(number)+'nd')
    elif number in aa and number == 3:
        print(str(number)+'rd')
numbers2=list(range(4,10))
for number2 in numbers2:
    print(str(number2)+'th')