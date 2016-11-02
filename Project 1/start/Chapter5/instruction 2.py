def getNum():
    run = True
    while run:
        num = input("Enter number.")
        if num.isdigit() and int(num) >= 0:
            return num
        else:
            print("Invalid input.")


def displayValue(resultName, resultValue):
    print(resultName + " is = " + resultValue)


def calcSum():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()


def calcProduct():
    run = True
    while run:
        try:
            num1 = int(input("Enter Number 1"))
            num2 = int(input("Enter Number 2"))
            print(num1 * num2)
            run = False
        except ValueError:
            print("Invalid Input.")


def getMinNum():
    run = True
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


def getMaxNum():
    run = True
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


def calcDifference():
    run = True
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


def calcQuotient():
    run = True
    while run:
        try:
            num1 = int(input("\nEnter Number 1"))
            num2 = int(input("Enter Number 2"))
            if num1 < num2:
                print(num2 / num1)
            else:
                print(num1 / num2)
            run = False
        except ValueError:
            print("Invalid Input.")


def main():
    calcSum()
    calcProduct()
    getMinNum()
    getMaxNum()
    calcDifference()
    calcQuotient()


main()