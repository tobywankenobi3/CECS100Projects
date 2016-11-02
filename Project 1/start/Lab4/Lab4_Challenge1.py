# Find win average over the past 5 years

# Input wins per year
year1 = int(input("How many wins in year 1?"))
year2 = int(input("How many wins in year 2?"))
year3 = int(input("How many wins in year 3?"))
year4 = int(input("How many wins in year 4?"))
year5 = int(input("How many wins in year 5?"))

# Get Average wins
totalWins = year1+year2+year3+year4+year5
avg = totalWins/5

# Display result
print("\nAverage number of wins is", avg)
