#!/usr/bin/env python
#
import operator as op

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]


def process_list(alist, func):  # <1>
    new_list = []
    for item in alist:
        new_list.append(func(item))  # <2>
    return new_list


f1 = process_list(fruits, str.upper)  # <3>
print(f1, "\n")

f2 = process_list(fruits, lambda s: s[0].upper())  # <4>
print(f2, "\n")

f3 = process_list(fruits, len)  # <5>
print(f3, "\n")

total_length = sum(process_list(fruits, len))  # <6>

print(total_length, "\n")

def process_pair(func, a, b):
    return func(a, b)

print(process_pair(op.add, 10, 15))
print(process_pair(op.mul, 10, 15))
print(process_pair(op.truediv, 10, 15))
print(process_pair(lambda x, y: x + y, 10, 15))

getter = op.itemgetter(2, 9, 3)

print(getter(fruits))