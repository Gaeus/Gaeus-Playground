cafeteria=input('How many times a week do you eat at the student cafeteria? ')
price=input('The price of a typycal student lunch? ')
groceries=input('How much do you spend on groceries per week? ')


# Calculate the total weekly expenditure
cafeteriaprice=float(cafeteria)*float(price)
totalweeklyexpenditure=cafeteriaprice+float(groceries)

# Calculate the daily expenditure
dailyexpenditure = totalweeklyexpenditure / 7


# Print the results
print("Average food expenditure:")
print(f"Daily: {dailyexpenditure} euros")
print(f"Weekly: {totalweeklyexpenditure} euros")
