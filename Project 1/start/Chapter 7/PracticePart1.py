import random

numList = []
max = 0
min = 0
total = 0
rand = 0

for i in range(20):
    rand = random.randint(0, 100)
    print("*",rand)
    numList.append(rand)

max = numList[0]
min = numList[0]

for i in numList:
    total += i
    if i < min:
        min = i
    if i > max:
        max = i

average = total/20
print("Maximum:", max, "\nMinimum:", min, "\nTotal:", total, "\nAverage:", average)
