#8-12
def make_sandwiches(person,*ingredients):
    print('\n' + person.title() + " wants its sandwich with the next ingredients: ")
    for ingredient in ingredients:
        print('-' + ingredient)

make_sandwiches('albeiro','pollo','pavo','green pepers','tomatoes sauch')
make_sandwiches('carmen','mayonesa','green pepers','tomatoes sauch')

#8-13 User profile
def user_profile(first,last,**user_info):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

my_own_profile=user_profile('albeiro','martinez',sexo='masculino',field='engeeniering')
print(my_own_profile)
