#!/usr/bin/env python
#
from operator import add, mul
from functools import reduce

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# sum()
result = reduce(add, values) # <1>
print("result is", result)

# sum() + 1000
result = reduce(add, values, 1000)  # <2>
print("result is", result)

# product
result = reduce(mul, values)  # <3>
print("result is", result)

strings = ['fee', 'fi', 'fo', 'fum']

# join
result = reduce(add, strings) # <4>
print("result is", result)

# join + upper case
result = reduce(add, map(str.title, strings))  # <5>
print("result is", result)

data = ['pastafazool', 5, 'foo', 6, 'bar', 7, 8, 4, 99, 'wombat']

def coerce(x):
    return x if isinstance(x, (int, float)) else 0

sum_of_data = reduce(lambda a, b: coerce(a) + coerce(b), data)
print(sum_of_data)

num = 1_000_000

# reduce(FUNC, iterable)
#  tr = FUNC(iterable[0], iterable[1]
#  tr = FUNC(tr, iterable[2])
#  tr = FUNC(tr, iterable[3])
# ...
def add(x, y):
    return x + y

values = 10, 20, 30, 40, 50

result = reduce(add, values)   # sum(values)
print(result)

result = reduce(mul, values)   # ?product?(values)
print(result)

data = ['pastafazool', 5, 'foo', 6, 'bar', 7, 8, 4, 99, 'wombat']

result = sum(n for n in data if isinstance(n, (int, float)))
print(result)

