
def spam(a, b):
    print(a, b)

spam(1, 2)
spam('ding', 'dong')

def ham(a, b, *args, c, d, **kwargs):
    print(a, b, c, d, args, kwargs)

ham("alpha", "beta", 1, 2, c="camel", d="dolphin",  w="walrus")
ham(1, 2, 3, 4, c=25, d=48, m="manatee", animal='wombat')
