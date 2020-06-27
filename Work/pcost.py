# pcost.py
#
# Exercise 1.27

import os
import gzip

total_cost = 0

with gzip.open("Data/portfolio.csv.gz", "rt") as f:
    next(f)
    for l in f:
        [shares, price] = l.split(",")[1:]
        total_cost = total_cost + int(shares) * float(price)

print(total_cost)
