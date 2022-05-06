from copy import deepcopy

x = 5  # create int obj; bind 'x' to it
y = x  # bind 'y' to same obj as 'x'

print("\U0001F92F")
print(x, type(x), id(x))
print(y, type(y), id(y))
print()

x = 10  # create int obj; bind 'x' to it
print(x, type(x), id(x))
print(y, type(y), id(y))

colors = [['eggs', 'ham'], 'red', 'green', 'purple']
c1 = colors  # alias

colors.append('pink')
print("colors: {}".format(colors))
print("c1: {}".format(c1))

# shallow copy
c2 = list(colors) # initialize list with colors
c2 = colors[:]  # full slice of colors

colors.append('brown')
print("colors: {}".format(colors))
print("c1: {}".format(c1))
print("c2: {}".format(c2))
print()
colors[0].append('spam')
print("colors: {}".format(colors))
print("c1: {}".format(c1))
print("c2: {}".format(c2))
print()

c3 = deepcopy(colors)
colors[0].append('toast')
print("colors: {}".format(colors))
print("c2: {}".format(c2))
print("c3: {}".format(c3))

print("id(colors[0]): {}".format(id(colors[0])))
print("id(c2[0]): {}".format(id(c2[0])))
print("id(c3[0]): {}".format(id(c3[0])))

def spam(animals):
    local_animals = deepcopy(animals)
    animals.append('wombat')
    # ham(animals)

beasts = ['lion', 'tiger', 'bear']
spam(beasts)
print("beasts: {}".format(beasts))
