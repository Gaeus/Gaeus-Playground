print("Welcome to the bill splitter v1.0!")
checkout = float(input("What was the total bill? :"))
tippercentage = int(input("What percentage tip would you like to give? Enter 0 if you're not socially pressured into it :"))
tip = 1+(tippercentage/100)
billcalculation = ( checkout * tip)
bill = (f"{billcalculation:.2f}")
print("okay, so you owe " + str(bill) + "€ to the restaurant." )
people = int(input("How many people to split the bill with? :"))
split = (float(bill) / people)
print(f"Each person should pay {split:.2f} €")