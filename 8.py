#  Write a program to remove the item present at index 4
#  and add it to the 2nd position and at the end of the list.

list1 = [54, 44, 27, 79, 91, 41]

list1.pop(3)
list1.append(79)
list1.insert(1, 79)

print(list1)