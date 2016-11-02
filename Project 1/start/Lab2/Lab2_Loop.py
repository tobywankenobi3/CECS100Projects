for i in ["Alan", "Alex", "Ally"]:
    name = input("What is " + i + "'s name?")
    whileAddress = input("What is " + i + "'s address?")
    whilePhone = input("What is " + i + "'s phone number?")
    whileMajor = input("What is " + i + "'s major?")
    print(name + ": Their address is", whileAddress, "Their phone number is", whilePhone, "and they are majoring in",
          whileMajor)

case = 0
while case >= 0:
    person = input("What is the person's name?")
    whileAddress = input("What is " + person + "'s address?")
    whilePhone = input("What is " + person + "'s phone number?")
    whileMajor = input("What is " + person + "'s major?")
    print(person + ": Their address is " + whileAddress + ", Their phone number is " + whilePhone +
          ", and they are majoring in " + whileMajor)
    case = int(input("Enter a positive value to continue loop, enter a negative value to end."))
