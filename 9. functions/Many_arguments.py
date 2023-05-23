#Passing an arbitrary Number of Arguments
def make_pizza(size, *toppings):
    #The * tell python to do a tupple with whatever number of
    #elements that we pass to the function
    '''Sumarize the pizza we are about to make'''
    print('\nMaking a ' + str(size) +
        '-inch pizza with the following toppings: ')
    for topping in toppings:
        print('- ' + topping.title())

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

#=====================================================================

#Using arbitrary keywords arguments
def build_profile(first,last,**user_info):
    #The double ** tell Python to create a dictionary
    '''Build a dictionary containing everything abouat an user'''
    profile={}#Se crea un dictionary vacio
    profile['first_name'] = first
    profile['last_name']= last
    for key, value in user_info.items():
        profile[key]=value
    return profile

user_profile = build_profile('albert',
    'eisntein', location='princeton',
    filed='phisycs')

print(user_profile)