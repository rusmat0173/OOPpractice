# Resource is this link: https://realpython.com/python3-object-oriented-programming/
# and https://www.datacamp.com/community/tutorials/python-oop-tutorial

class Dog:

    # class attribute
    species = 'mammal'

    # Initialise and initial attributes
    def __init__(self, name, age, buddy=None):
        self.name = name
        self.age = age
        self.buddy = buddy

    def bark(self):
        print('woof, woof')

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

ozzy = Dog('Ozzy', 2)

print(ozzy.name, ozzy.age)
ozzy.bark()

skippy = Dog('Skippy', 12)
skippy.age = 11
print(skippy.age)

filou = Dog('Filou', 5)

ozzy.setBuddy(skippy)
print(ozzy.buddy.name, skippy.buddy.name)

# can only have one buddy,, the way set up here
ozzy.setBuddy(skippy)
print(ozzy.buddy, skippy.buddy)

# add an attribute from outside the class definition <= but not pythonic!
filou.owner = 'John'
print(filou.owner)

# use of getattr. Note construction and use attribute as a string
# https://www.journaldev.com/16146/python-getattr
""" The main reason to use python getattr() is that we can get the value by using the name of the attribute as String. 
So you can manually input the attribute name in your program from console."""
print(getattr(skippy,'age'))

# use of setattr. Note construction and use attribute as a string
setattr(skippy, 'age', 16)
print(skippy.age)

# use of hasattr. Note construction and use attribute as a string
print(hasattr(skippy, 'buddy'))
print(hasattr(filou, 'owner'))
print(hasattr(ozzy, 'owner'))


