from random import choice

class RandomWord:
    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._words = words_in.read().splitlines()

    def get_random_word(self):
        return choice(self._words)

rw1 = RandomWord()
for _ in range(10):
    print(rw1.get_random_word())
print('-' * 60)

class RandomWordCallable:
    def __init__(self):
        with open('DATA/words.txt') as words_in:
            self._words = words_in.read().splitlines()

    def __call__(self):
        return choice(self._words)

get_word = RandomWordCallable()
for _ in range(10):
    print(get_word())  # get_word.__call__()
print('-' * 60)

class Junk:
    def __call__(self):
        print("in __call__()")

Junk()()

