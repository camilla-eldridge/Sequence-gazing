#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd

number=sys.argv[1]

def fibonacci(n):
    fib_seq = np.zeros(n, dtype=int)
    fib_seq[1] = 1
    for i in range(2, n):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    return fib_seq

# Specify the length of Fibonacci sequence (arg[1])
number=int(number)

# Generate Fibonacci sequence
sequence=fibonacci(number)

# Create a pandas dataframe to store and index the Fibonacci sequence
sequence_df = pd.DataFrame({'Index': range(number), 'Fibonacci Number': sequence})

# print the dataframe 
print(sequence_df[1:])

