class Animal:
    pass

class Cat(Animal):
    def meow(self):
        print("meow meow")

c1 = Cat()
c1.meow()
print("type(c1): {}\n".format(type(c1)))

class_name = 'Dog'
bark_method = lambda self: print("Woof woof")
default_breed = "mixed"

Dog = type(
    class_name,
    (Animal,),
    {
        'breed': default_breed,
        'bark': bark_method,
    }
)
d1 = Dog()
d1.bark()
print(d1.breed)
