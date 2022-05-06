#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from collections.abc import Sized, Iterator  # <1>


class BadContainer(Sized):  # <2>
    pass


class GoodContainer(Sized):
    def __len__(self):   # <3>
        return 42


try:
    bad = BadContainer()  # <4>
except TypeError as err:
    print(err)  # <5>
else:
    print(bad)

print()

try:
    good = GoodContainer()  # <6>
except TypeError as err:
    print(err)
else:
    print(good)  # <7>
    print(len(good))  # <8>

print()


class MyIterator(Iterator):  # <9>
    def __init__(self):
        self._data = 'a', 'b', 'c'
        self._index = 0

    # def __iter__(self):
    #     return self

    def __next__(self):  # <10>
        if self._index >= len(self._data):
            raise StopIteration
        else:
            return_val = self._data[self._index]
            self._index += 1
            return return_val


m = MyIterator()  # <11>
for i in m:  # <12>
    print(i)
print()

print(hasattr(m, '__iter__'))  # <12>

class Flyer(metaclass=ABCMeta):
    def bark(self):
        print("WOOF WOOF!")

    @abstractmethod
    def fly(self):
        pass

class Duck(Flyer):
    def fly(self):
        print("FLYING....")

    def bark(self):
        raise NotImplementedError("I don't know how to bark!")

d = Duck()
d.fly()
# d.bark()

class Dodo(Flyer):
    pass

# do = Dodo()
# do.fly()

class Spam:
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return self._value + other._value

    def __len__(self):
        return 1000000

s1 = Spam(25)
s2 = Spam(16)
print(s1 + s2)
print(len(s1))


print(good.__len__())

def barf(self):
    return 989

from types import MethodType
setattr(good, '__len__', MethodType(barf, good))

print(len(good))




