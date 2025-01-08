numberinput = input("Please type in a number:")
absolute= int(numberinput)
negativeabsolute = int(numberinput)*(-1)

if int(numberinput) < 0:
    print("The absolute value of this number is " + str(negativeabsolute))
elif int(numberinput) >= 0:
    print("The absolute value of this number is " + str(absolute))