number1=input("Enter first number: ")
number2=input("Enter second number: ")
operation=str.lower(input("Enter operation:Add, Subtract, Multiply, Divide: "))
if operation=="add" or operation=="+":
    print(f"{number1} + {number2} = {float(number1)+float(number2)}")
elif operation=="substract" or operation=="-":
    print(f"{number1} - {number2} = {float(number1)-float(number2)}")
elif operation=="multiply"  or operation=="*":
    print(f"{number1} * {number2} = {float(number1)*float(number2)}")
elif operation=="divide"or operation=="/":
    print(f"{number1} / {number2} = {float(number1)/float(number2)}")

else:
    print("Invalid operation")