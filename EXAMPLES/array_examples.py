#!/usr/bin/env python
from sys import getsizeof
from array import array
from random import randint
import numpy as np

values = [randint(1, 30000) for i in range(1000)]  # <1>

print(f'Size of integer list: {getsizeof(values)}\n')

for datatype in 'i', 'h', 'L', 'Q', 'd':
    data_array = array(datatype, values)  # <2>
    print(f'Size of {datatype} array: {getsizeof(data_array)}  Contents:',
          data_array[:5], '...')  # <3>
    print()

npa  = np.array(values, dtype=np.uint16)
print(f'Size of numpy array: {getsizeof(npa)}  Contents:',
      npa[:5], '...')  # <3>

