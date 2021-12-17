#  Given two lists, l1 and l2,
#  write a program to create a third list l3 by picking an odd-index element from the list l1
#  and even index elements from the list l2.

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = l1 + l2
l4 = []

for i in l3:
    if i % 2 == 1:
        l4.append(i)
print(l4)
