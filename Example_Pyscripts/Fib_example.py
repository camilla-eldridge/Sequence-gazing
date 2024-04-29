#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

number=sys.argv[1]

def fibonacci(n):
    fib_seq = np.zeros(n, dtype=int)
    fib_seq[0] = 1
    fib_seq[1] = 1
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    return fib_seq

# Specify the length of Fib sequence (arg[1])
number=int(number)

# Generate Fib sequence
sequence=fibonacci(number)

# Create a pandas dataframe to store and index Fib sequence
sequence_df = pd.DataFrame({'Index': range(number), 'Fibonacci Number': sequence})

# Make the index more human readible (add 1 to index column)
sequence_df['Index'] += 1

# print the dataframe 
print(sequence_df[1:])

