
# function counts how many instances of a belt color in the dictionary


def belt_count(dictionary):

    belts = list(dictionary.values())
    # created a set so that it will loop thorugh.
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


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


# ninja_intro(ninja_belts)
belt_count(ninja_belts)
