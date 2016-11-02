#Get Starting Amount and Display
amount = float(input("How much is the sale?"))
print("Original Sale:", amount)

#Get sales and county tax
sTax = format(amount *.05, '.2')
cTax = format(amount*.025, '.2')

#Display Taxes
print("Sales Tax:", sTax)
print("County Tax:", cTax)

#Display Total Tax
totalTax = float(sTax) + float(cTax)
print("Total Tax:", totalTax)

#Display Total Sale
total = totalTax + amount
print("Total Sale:", total)