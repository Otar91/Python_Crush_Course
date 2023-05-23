#Passing a list to a function
def greeting_users(names):
    '''Print a simple greeting to each user in the list'''
    for name in names:
        msg= 'Hello, ' + name.title() +'!'
        print(msg)

usernames=['Joseph','federico','noah']

greeting_users(usernames)

#modifying a list in a function
def print_models(unprinted_desings, completed_models):
    '''Simulate printing each desing, until none are left.
        Move each desing to completed_models after printing.'''

    while unprinted_desings:
        current_desing=unprinted_desings.pop()

        #Simulate creating a 3D print from de desing
        print('Printing model: ' + current_desing)
        completed_models.append(current_desing)

def show_completed_models(completed_models):
    '''Show all the models that were printed'''
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

unprinted_desings=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)

print(completed_models)
