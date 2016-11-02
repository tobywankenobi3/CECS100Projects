# Sean Curley
# Sept. 14 2016
# Program to have a user input their name, major, and credits taken.  Then output the credits
# taken and still required
#
# Input values
name = input("\nWhat is your name?")
major = input("\nWhat major program are you in?")
creditsDegree = input("\nHow many credits do you need to graduate?")
creditsTaken = input("\nHow many credits have you taken?")

# Set values for Display
creditsLeft = float(creditsDegree) - float(creditsTaken)

# Display variables
print("\n",name, "is in the", major, "program.")
print(major,  "requires", creditsDegree, "credits and he/she has taken", creditsTaken, "credits.")