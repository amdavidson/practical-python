# bounce.py
#
# Exercise 1.5

current_height = 100
bounce_factor = 3 / 5
bounce_number = 1


while bounce_number <= 10:
    current_height = current_height * bounce_factor
    print(bounce_number, round(current_height, 4))
    bounce_number += 1
