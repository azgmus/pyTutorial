from collections import Counter


list1 = ["pizza", "burger", "burger",
         "pizza", "cheese", "burger",
         "pizza", "cheese", "burger"]

list1.insert(3, "inserted Value")


while list1.count("pizza"):
    list1.remove("pizza")
print(Counter(list1))