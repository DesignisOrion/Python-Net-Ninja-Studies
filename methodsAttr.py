class Planet:

    # class level attributes
    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        # instance attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # a method attached to the class
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    # class methods on the instance
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} beacuse of gravity'

    # static methods on the instance
    @staticmethod
    def spin(speed='20000 miles per hour'):
        return f'The planet spins and spins at {speed}'


print(naboo.spin('a very high speed'))
