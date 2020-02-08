class Person(object):

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self.__last_name = last_name

    def fullname(self):
        return '{}, {}'.format(self.__last_name, self._first_name)

    def say_hello(self):
        print('Hi there, my name is {} {}'.format(self._first_name, self.__last_name))

    def __str__(self):
        return '{}, {}'.format(self.__last_name, self._first_name)
    


a = Person('John', 'Smith')
print(a.fullname())
print(a._first_name)
# print(a.__last_name)  # AttributeError: 'Person' object has no attribute '__last_name'
print(a)
a.say_hello()
