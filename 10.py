#  Write a program to iterate a given list
#  and count the occurrence of each element
#  and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(dict((i, sample_list.count(i)) for i in sample_list))

# ჩემ ფეხებს დავწერდი ამას, stackoverflow-ს მადლობა

