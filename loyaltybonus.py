points=int(input("How many loyalty points do you have? :"))
if points<100:
    bonus=1.1
    print("Your bonus is 10%")
    
else:
    bonus=1.15
    print("Your bonus is 15%")

print(f"You now have {int(points*bonus)} points")