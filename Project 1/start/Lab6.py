# Get input variables
height = input("How tall are you, in inches?")
weight = input("How much do you weigh?")

# Calculate and output BMI
bmi = float(weight * (703/(height**2)))
print("Your BMI index is", bmi, ".")

#Check for optimal BMI
if bmi >= 18.5 and bmi <= 25:
    print("You are at an optimal weight.")
elif bmi < 18.5:
    print("You are slightly underweight")
elif bmi > 25:
    print("You are slightly overwieght")

# End program