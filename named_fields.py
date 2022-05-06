from collections import namedtuple
from dataclasses import dataclass
#
person = 'Bill', 'Gates', 'Microsoft', 1955
print(person[0], person[1], '\n')


def spam(person_data):
    print(person_data[0], person_data[1])

spam(person)
print()

Person  = namedtuple('Person', 'first_name last_name product birth_year')

p1 = Person("Bill", "Gates", "Microsoft", 1955)
p2 = Person("Mickey", "Mouse", "Disney", 1936)

for p in p1, p2:
    print(p.first_name, p.last_name)
print()

def print_person(data):
    print(data.first_name, data.last_name)

print_person(p1)
print_person(p2)

@dataclass
class ComputerPerson:
    first_name: str
    last_name: str
    product: str
    birth_year: int

    def bark(self):
        print("Woof! Woof!")

p = ComputerPerson('Bill', 'Gates', 'Microsoft', 1954)
print(p)
print(p.first_name, p.last_name)
p.bark()
