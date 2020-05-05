# This is a global variable because it is outside of the function
my_name = 'Orion'


def print_name():
    global my_name
    # local scope of the variable
    my_name = 'Micah'
    print('the name inside the function is', my_name)


print_name()
print('outside the function the name is', my_name)
