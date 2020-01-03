# Ex 4., in https://www.cs.uct.ac.za/mit_notes/python/Classes.html

class Numbers:

    # single class attribute
    MULTIPLIER = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Class attribute is {}, instance attributes are {} and {}'.format('MULTIPLIER', self.x, self.y)

    # write a method called add that adds x and y
    # technically this is an 'instance method'
    def add(self):
        return self.x + self.y

    # write a class method called add that multiplies a by class attribute
    # class method belongs to a class, not an instance
    @classmethod # <= decorator, you don't need this for it to work
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    # https://www.journaldev.com/18722/python-static-method
    # write a static method called subtracts c from b
    # i.e. method belongs to class rather than an instance/object, e.g. can call from Numbers class
    @staticmethod # <= decorator, you don't need this for it to work
    def subtract(b, c):
        return b - c

    # for @property, see https://www.machinelearningplus.com/python/python-property/


num = Numbers(3,9)
print(num.add())
print(num.multiply(11))

print(num.subtract(3,4))
print(Numbers.subtract(3,2))

print(str(num))
