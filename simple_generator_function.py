import sys

letters = ['a', 'b', 'c']

def abcs():
    yield 'a'
    yield 'b'
    yield 'c'

a = abcs()
print("a: {}".format(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

print("sys.getsizeof(letters): {}".format(sys.getsizeof(letters)))

x = abcs()
print("x: {}".format(x))
print("BEFORE: sys.getsizeof(x): {}".format(sys.getsizeof(x)))

for letter in x:
    # next(x) ...
    print("letter: {}".format(letter))
print("AFTER: sys.getsizeof(x): {}".format(sys.getsizeof(x)))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fgen = (f.upper() for f in fruits)

print("sys.getsizeof(fruits): {}".format(sys.getsizeof(fruits)))
print("sys.getsizeof(fgen): {}".format(sys.getsizeof(fgen)))

numbers_a = list(range(10000))
numbers_b = (n * 1 for n in range(10000))
print("sys.getsizeof(numbers_a): {}".format(sys.getsizeof(numbers_a)))
print("sys.getsizeof(numbers_b): {}".format(sys.getsizeof(numbers_b)))

num_list = [2 * n for n in range(1_000)]
num_gen = (2 * n for n in range(1_000))
print("sys.getsizeof(num_list): {}".format(sys.getsizeof(num_list)))
print("sys.getsizeof(num_gen): {}".format(sys.getsizeof(num_gen)))
for n in num_gen:
    print(n)
print("sys.getsizeof(num_gen): {}".format(sys.getsizeof(num_gen)))




