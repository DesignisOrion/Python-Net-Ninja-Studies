# Creating a function that cycles through all that was entered by user once out the loop.
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


# This is an empty dictionary
ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    # The user may want to add another belt
    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break


ninja_intro(ninja_belts)
