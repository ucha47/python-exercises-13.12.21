#  Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#  and write a program that returns a list
#  that contains only the elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.
#  Extras: Randomly generate two lists to test this

import random

first_list = []

for i in range(0, 8):
    a = random.randint(0, 100)
    first_list.append(a)

second_list = []

for i in range(0, 10):
    b = random.randint(0, 100)
    second_list.append(b)

print(first_list)
print(second_list)
print('-----------------------------------------')

common = []

for a in first_list:
    if a in second_list:
        if a not in common:
            common.append(a)
print(common)

# JOBDA a = range(1, random.randint(1, 100))


