#!/usr/bin/env python

def next_prime(limit):
    non_prime = set()  # <1>

    for i in range(2, limit):
        if i in non_prime:
            continue
        for j in range(2 * i, limit + 1, i):
            non_prime.add(j)  # <2>
        yield i  # <3>

limit = 50_000_000
np = next_prime(limit)  # <4>
count = 0
for prime in np:  # <5>
    # print(prime, end=' ')
    count += 1
print(f"{count} primes under {limit}")