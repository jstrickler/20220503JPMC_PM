from itertools import chain

a = "abc"
b = [1, 2, 3]
c = 'spam', 'ham', 'eggs', 'toast'

for thing in a, b, c:
    print(thing)
print('-' * 60)


for thing in chain(a, b, c):
    print(thing)
print('-' * 60)

animals = [['cat', 'dog', 'gerbil'],
           ['lion', 'tiger', 'jaguar'],
            ['wallaby', 'quokka', 'wombat']]



for thing in animals:
    print(thing)
print('-' * 60)

from collections import Counter
for thing in chain.from_iterable(chain.from_iterable(animals)):
    print(thing, end=',')
print('-' * 60)

c = Counter(chain.from_iterable(chain.from_iterable(animals)))
print(c)