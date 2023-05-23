def get_formatted_name(first_name, last_name):
    '''Return a full name neatly formatted'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician) 
#======================================================================

#Functions with opcional values
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name= first_name + ' ' + middle_name + " " + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

musician = get_formatted_name('jhon','lee',middle_name='hooker')
print(musician)
        
#return a dictionary
def build_person(first_name,last_name):
    '''Return of information about persons'''
    person={'first':first_name,'last':last_name}
    return person

musician=build_person('jimi','hendrix')
print(musician)
