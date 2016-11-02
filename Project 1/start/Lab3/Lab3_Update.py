STATE = .05
COUNTY = .025


def getAmount():
    amountPurchase = float(input('Enter purchase amount: '))
    while amountPurchase <= 0:
        amountPurchase = float(input('Cannot process 0 or less, please enter another number: '))
    return amountPurchase


def calculateSales(amountPurchase):
    sales = amountPurchase * STATE
    return sales


def calculateCounty(amountPurchase):
    county = amountPurchase * COUNTY
    return county


def taxTotal(amountPurchase):
    taxTotal = calculateSales(amountPurchase) + calculateCounty(amountPurchase)
    return taxTotal


def calculateTotal(amountPurchase, totalTax):
    total = (totalTax + amountPurchase)
    return total


def displayTotal(amountPurchase, sales, county, totalTax, total):
    print('\nPurchase: ', "%.2f" % amountPurchase, '\nSales tax: ', "%.2f" % sales, '\nCounty tax: ', "%.2f" % county)
    print('Total Tax: ', "%.2f" % totalTax, '\nTotal Sale: ', "%.2f" % total)


def main():
    amountPurchase = getAmount()
    sales = calculateSales(amountPurchase)
    county = calculateCounty(amountPurchase)
    totalTax = taxTotal(amountPurchase)
    total = calculateTotal(amountPurchase, totalTax)
    displayTotal(amountPurchase, sales, county, totalTax, total)


main()
