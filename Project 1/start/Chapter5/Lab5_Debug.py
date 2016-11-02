def getNum():
    run = True
    while run:
        num = input("Enter number.")
        if num.isdigit() and int(num) >= 0:
            return num
        else:
            print("Invalid input.")

def main():
    print(getNum())
    print(getNum())

main()