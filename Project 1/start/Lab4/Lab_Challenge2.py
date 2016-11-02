# Program to get calories burned per mile by steps taken

# Set variables
stepsTaken = int(input("How many steps did you take today?"))

# Calculate miles and calories
miles = float(stepsTaken)/2000
calories = miles * 65

# Format and print calories burned
print("You burned ", format(calories,"2"), "calories!")
