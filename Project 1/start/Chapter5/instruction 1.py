run = True

num1 = 0
num2 = 0
# add
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        run = False
        print(num1 + num2)
    except ValueError:
        print("Invalid Input.")

run = True

# multiply
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        print(num1 * num2)
        run = False
    except ValueError:
        print("Invalid Input.")

run = True

# print larger number
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        if num1 > num2:
            print(num1)
        else:
            print(num2)
        run = False
    except ValueError:
        print("Invalid Input.")

run = True

# print smaller number
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        if num1 < num2:
            print(num1)
        else:
            print(num2)
        run = False
    except ValueError:
        print("Invalid Input.")

run = True

# subtract
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        if num1 < num2:
            print(num2 - num1)
        else:
            print(num1 - num2)
        run = False
    except ValueError:
        print("Invalid Input.")
run = True

# divide
while run:
    try:
        num1 = int(input("Enter Number 1"))
        num2 = int(input("Enter Number 2"))
        if num1 < num2:
            print(num2 / num1)
        else:
            print(num1 / num2)
        run = False
    except ValueError:
        print("Invalid Input.")
