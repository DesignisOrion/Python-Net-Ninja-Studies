# def greet():
#     print('Hello, World!')


# greet()


# Pass data in the function
# def greet(name, time):
#     print(f'Good {time}{name}, hope you are well')


# name = input('enter your name: ')
# time = input('enter the time of day: ')


# greet(name, time)


# Another way to call objects in a function

# def greet(name='Orion', time='morning'):
#     print(f'Good{time} {name}, hope you are well')


# greet()

# In this example, anything that's called overides the function


# def greet(name='Orion', time='morning'):
#     print(f'Good{time} {name}, hope you are well')


# greet(name="Micah")


def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)


radius = int(input('Enter a radius: '))
length = int(input('Enter a length:'))
area(radius)


area_calc = area(radius)
vol(area_calc, length)
