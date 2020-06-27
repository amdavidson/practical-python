# pcost.py
#
# Exercise 1.27

import os
import csv


def portfolio_cost(filename):
    "returns total cost of the portfolio from filename"
    total_cost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        next(rows)
        for l in rows:
            try:
                [shares, price] = l[1:]
                total_cost = total_cost + int(shares) * float(price)
            except:
                print("Could not parse:", l)
    return total_cost


total_cost = portfolio_cost("Data/missing.csv")
print("Total cost:", total_cost)
