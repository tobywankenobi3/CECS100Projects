def getNum():
    run = True
    while run:
        num = input("Enter number.")
        if num.isdigit() and int(num) >= 0:
            return int(num)
        else:
            print("Invalid input.")


def displayValue(resultName, resultValue):
    print(resultName + " is = " + str(resultValue))


def calcSum():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        add = num1 + num2
        displayValue("Addition", add)
        run = False


def calcProduct():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        add = num1 * num2
        displayValue("Multiplication", add)
        run = False


def getMinNum():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        if num1 < num2:
            displayValue("Greater", num1)
        else:
            displayValue("Greater", num2)
        run = False


def getMaxNum():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        if num1 > num2:
            displayValue("Lesser", num1)
        else:
            displayValue("Lesser", num2)
        run = False


def calcDifference():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        if num1 < num2:
            minus = num2 - num1
            displayValue("Subtraction", minus)
        else:
            minus = num1 - num2
            displayValue("Subtraction", minus)
        run = False


def calcQuotient():
    run = True
    while run:
        num1 = getNum()
        num2 = getNum()
        if num1 < num2:
            quotient = num2/num1
            displayValue("Division", float(quotient))
        else:
            quotient = num1/num2
            displayValue("Division", float(quotient))
        run = False


def main():
    calcSum()
    calcProduct()
    getMaxNum()
    getMinNum()
    calcDifference()
    calcQuotient()

main()