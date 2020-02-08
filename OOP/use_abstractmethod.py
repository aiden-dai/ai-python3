from abc import ABC, abstractmethod

class Foo(ABC):
    @abstractmethod
    def fun(self):
        '''please Implemente in subclass'''
        pass


class SubFoo(Foo):
    def fun(self):
        print('fun in SubFoo')



# a = Foo()  # TypeError: Can't instantiate abstract class Foo with abstract methods fun
a = SubFoo()
a.fun()

