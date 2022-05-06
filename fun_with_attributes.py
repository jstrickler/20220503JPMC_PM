
#  @classmethod @staticmethod

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self.color = "red"

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

c1 = Card('8', 'Diamonds')
c2 = Card('2', 'Clubs')
print(c1, c2)

colors = ['red', 'blue', 'yellow']
print(dir(colors))

print()

print("dir(c1): {}\n".format(dir(c1)))

print(c1.rank)

attrs = ['rank', 'suit']

for attr in attrs:
    print(getattr(c1,attr))

# getattr(obj, name)
# hasattr(obj, name)
# setattr(obj, name, value)
# delattr(obj, name)

 # to_json()

if hasattr(c1, 'to_json'):
    result = c1.to_json()
else:
    pass # do custom thing here...

setattr(c1, 'value', 22)

print(c1.value)

class Dog:
    pass

d1 = Dog()

setattr(Dog, 'bark', lambda self: print("woof!!"))

d1.bark()

delattr(Dog, 'bark')

# d1.bark()

setattr(Dog, 'breed', 'English Shepherd')

print(d1.breed)

