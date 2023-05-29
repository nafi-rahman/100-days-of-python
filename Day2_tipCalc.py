bill = float(input("what\'s the total bill?"))

percent = float(input("what\'s the percentage of the tip"))

numP = float(input("how many people will split the bill?"))

finalBill = round(((bill * (percent/100)) + bill) / numP, 2)

print(finalBill)