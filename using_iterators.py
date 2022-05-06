
x = [1, 2, 3]  # x is an iterable, but not
               # an iterator

for value in x:
    print(value)
print()

x_iter = iter(x)
print("x_iter: {}".format(x_iter))
for item in x_iter:
    print(item)

x_iter = iter(x)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
# print(next(x_iter))

with open('DATA/tyger.txt') as tyger_in:
    for raw_line in tyger_in: # next() next() next()
        line = raw_line.rstrip()
        print(line)
        try:
            next(tyger_in)  # consume next value
        except StopIteration:
            pass
import csv
with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    # headers = next(rdr)  # consume 1st line
    for row in rdr:
        print(row[2], row[1])
print('-' * 60)