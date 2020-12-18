list1 = ["0","1","2", "3", "4",
         "5", "6","20","8", "9",
         "10", "11","12", "13"]

print(sorted(list1, key=int))

# (sort1) list1.sort()

print(list1)

# (3)for item_index in range(len(list1)//2):
# (3)   list1[item_index], list1[-item_index -1] = list1[-item_index-1], list1[item_index]

# (2)list1[:] = reversed(list1)
# (2)list1.reverse()

# (1)[list1.remove(item) for item in list1 if item == 'pizza']

