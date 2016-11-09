## TRUE values: [4,9,2],[3,5,7],[8,1,6]

# Get number validated to digit, <9
def getNumber():
    run = True
    while run:
        num = input("Enter a value:")
        if num.isdigit() and int(num) <= 9:
            return int(num)
        else:
            print("Invalid input, please re-enter.\n")


# Get matrix, making sure the number has not been used yet
def getMatrix():
    run = True
    nums = []
    a = []
    b = []
    c = []
    placeNum = 0
    for i in range(3):
        while run:
            placeNum = getNumber()
            if nums.count(placeNum) == 0:
                a.append(placeNum)
                nums.append(placeNum)
                run = False
            else:
                print("Number already used.  Please enter a new number.")
        run = True
    print(a)
    for i in range(3):
        while run:
            placeNum = getNumber()
            if nums.count(placeNum) == 0:
                b.append(placeNum)
                nums.append(placeNum)
                run = False
            else:
                print("Number already used.  Please enter a new number.")
        run = True
    print(b)
    for i in range(3):
        while run:
            placeNum = getNumber()
            if nums.count(placeNum) == 0:
                c.append(placeNum)
                nums.append(placeNum)
                run = False
            else:
                print("Number already used.  Please enter a new number.")
        run = True
    print(c)
    matrix = [a,b,c]
    print(matrix)
    return matrix


# Get all Matrix row, column, and Diagonal Values added up
def getValues(matrix):
    row1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
    row2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
    row3 = matrix[2][0] + matrix[2][1] + matrix[2][2]
    col1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
    col2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
    col3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
    dia1 = matrix[0][2] + matrix[1][1] + matrix[2][0]
    dia2 = matrix[0][0] + matrix[1][1] + matrix[2][2]
    values = [row1, row2, row3, col1, col2, col3, dia1, dia2]
    return values


# Check Matrix Values [getValues()] to b equal to 15
def checkSquare(matrix):
    bool = True
    values = getValues(matrix)
    for element in range(8):
        place = values[element]
        if not place == 15:
            print("\nNot a Lo Shu Magic Square")
            bool = False
            break
    if bool == True:
        print("Your square is a Lo Shu Magic Square!")


def main():
    run = True
    while run:
        matrix = getMatrix()
        checkSquare(matrix)
        while run:
            check = input("Would you like to check another Square?\tY/N")
            if check.lower() == "n":
                run = False
            elif check.lower() == "y":
                break
            elif not check.lower() == "y":
                print("Invalid input, Please re-enter.\n**")


main()
