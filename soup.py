name=input("Please tell me your name: ")
soupcost=5.9
if name.lower() == "jerry":
    print("Next please!")
else:
    soupinput=int(input("How many portions of soup? "))
    totalcost= soupinput*soupcost
    print(f"The total cost is {totalcost}")
    print("Next please!")