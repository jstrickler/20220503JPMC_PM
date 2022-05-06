from itertools import groupby

pres_data = []
with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        _, last_name, first_name, *_, party = line.split(':')
        record = first_name, last_name, party
        pres_data.append(record)

pres_data.sort(key=lambda p: (p[2], p[1], p[0]))

pres_grouped = groupby(pres_data, key=lambda p: p[2])
print(pres_grouped)
for party, pres_list in pres_grouped:
    last_names = [f"{p[0]} {p[1]}" for p in pres_list]
    print(party, last_names)

from itertools import product

ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()
suits = 'Clubs Diamonds Hearts Spades'.split()
cards = product(ranks, suits)
print(list(cards))



