nameList = ["Suzy", "Lillie", "Benjamin", "Abbie", "Olivia", "Jeff", "Chloe", "Daisy", "Raymond", "Simon"]

# print the list
print(nameList)
# print the 5th item in the list
print(nameList[4])
# Change element 10 to 100 and print
element = nameList[9]
nameList.remove(element)
nameList.append(100)
print(nameList)
# Remove element 10 and print
nameList.remove(nameList[9])
print(nameList)
# insert the name "Joy" into element 10 and print
nameList.insert(9, "Joy")
print(nameList)
# print elements 7 thru 12 - slice of the list
for i in range(4,7):
    print(nameList[i])
# Search for the name "joy" in the list and print result
print("Index of 'Joy':",nameList.index("Joy"))
# Sort the list in ascending order and print
nameList.sort()
print(nameList)
# Reverse the order of the list and print
nameList.reverse()
print(nameList)
#Delete the name "joy" from the list using del and print
index = nameList.index("Joy")
del(nameList[index])
print(nameList)