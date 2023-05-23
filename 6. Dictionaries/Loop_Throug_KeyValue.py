user_0={'username':'efermi','first':'enrico','last':'fermi'};

for key,value in user_0.items():
    #into the for loop the names 'key' and 'value' are just names to move througt the dictionary so, you can use every name that you want
    #Example for k,v in ....
    #items() method return a list for key-values pairs in the dictionary
    print('\nKey: ' + key);
    print('Value: ' + value);

favorite_lenguages= {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
    }

for key, value in favorite_lenguages.items():
    print('\n '+key.title() + ' has '+ value.title() + ' like his favorite lenguage.')

#==============================================================================================
#Looping through all the keys  in a Dictionary
favorite_lenguages= {
    'jen':'python',
    'sarah': 'c',
    'edward':'ruby',
    'phil':'python',
    }

#The keys() method se usa para acceder solo a la informacion de las keys dentro de un diccionario
for name in favorite_lenguages.keys():#keys methods se puede omitir y se conseguira el mismo resultado
    #que los nombres de las keys se almacenen de a uno en la variable name
    print(name.title())

friends=['phil','sarah']
for name in friends:
    print('\nHi ' + name.title())

    if name in favorite_lenguages:
        print('Hi ' + name.title() + ', I see your favorite lenguage is '
        + favorite_lenguages[name].title() 
        )
#probar si hay una key dentro de un diccionario
if 'Erick' not in favorite_lenguages.keys():
    print('\nPlease Erick take our poll!')