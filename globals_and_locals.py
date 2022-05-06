import sys

def spam():
    word = " spam"
    print(word * 3)

animal = "wombat"

spam()

g = globals()
print("g: {}".format(g))

print(g['animal'])
print(animal)

g['color'] = "teal"
print(color)

g['bark'] = lambda : print("woof! woof!")

bark()

condiment = "chutney"


#  local -> nested -> global -> builtin
def ham(cheese, mustard):
    # condiment = "relish"
    print("in ham: condiment: {}".format(condiment))

    print("locals(): {}".format(locals()))

ham('swiss', 'Grey Poupon')
print("condiment: {}".format(condiment))
