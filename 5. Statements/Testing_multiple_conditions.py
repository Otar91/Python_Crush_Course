#Testing multiple conditions
#one option to test multiple conditions and not omitting someone is to use a series of 'if' statements

requested_toppins=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppins:
    print('Adding mushrooms');
#The second and third tests are executed regardless the result in previous test
if 'pepperoni' in requested_toppins:
    print('adding pepperoni');
if 'extra cheese' in requested_toppins:
    print('Adding extra cheese');
print('\n Finished making your pizza');