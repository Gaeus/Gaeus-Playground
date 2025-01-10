money=float(input("Enter the amount of money you earn per hour: "))
hours=float(input("How many hours do you work per day? : "))
day=input("Which day of the week is it? : ")
if day.lower()=="sunday":
    print("Daily wages:",money*hours*2,"euros")
else:
    print("Daily wages:",money*hours,"euros")