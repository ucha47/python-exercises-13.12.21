#  Slice list into 3 equal chunks and reverse each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

list1 = sample_list[:3]
list2 = sample_list[3:6]
list3 = sample_list[6:]
list1.reverse()
list2.reverse()
list3.reverse()

print(list1)
print(list2)
print(list3)