#Start with user that need to be confirmed
#and a empty list to hold confirmed users
unconfirmed_users=['alice','brian','candece']
confirmed_users=[]
#verify each user until there are not more unconfirmed users
#move to verificed user into the list confirmed users
while unconfirmed_users: #Corre hasta que la lista no este vacia
    current_user=unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

#display all confirmed users
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#============================================================================
#removing all instances of specific value from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#=============================================================================
#Filling a dictionary with user input

responses = {}

#set a flag to indicates the polling is active
polling_active=True

while polling_active:
    #prompt for the person's name and response.
    name = input('\nWhats your name?\n')
    response = input('Witch mountain do you like to climb someday?\n')

    #store the renponse in the dictionary
    responses[name] =   response

    #find out if anyone else is going to take poll
    repeat = input('Would you like to let another person repond (yes/no)\t')
    if repeat == 'no':
        polling_active = False

#polling is complete. Show the results
print('\n--- Poll Results---')
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() + '.' )