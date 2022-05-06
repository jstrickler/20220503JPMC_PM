#!/usr/bin/env python
#

strings = ['wombat', 'koala', 'kookaburra', 'blue-ringed octopus']

result = [s.upper() for s in strings]  # <1>
print(result)

result = list(map(str.upper, strings))  # <2>
print(result)

result = list(map(len, strings))  # <3>
print(result)

m1 = map(str.upper, strings)   # map object
g1 = (s.upper() for s in strings)  # generator expression
print(m1, g1)
for s in m1:
    print(s)
print('-' * 60)
for s in g1:
    print(s)