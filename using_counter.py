from collections import Counter

c = Counter()

food = ['spam', 'spam', 'spam', 'spam',
        'spam', 'ham', 'ham', 'spam', 'eggs']

for f in food:
    c[f] += 1  # default value is 0

print("c: {}".format(c))

c = Counter(food)
print("c: {}".format(c))
print()

with open('DATA/words.txt') as words_in:
    first_letters = (w[0] for w in words_in)
    letter_counts = Counter(first_letters)

print("letter_counts: {}".format(letter_counts))
print()

print(letter_counts.most_common(5))