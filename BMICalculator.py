height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = ((weight/(height**2))*10000)

print("Your BMI is " + str(int(bmi)))


if bmi < 16:
    print("You are severily underweight")
elif 16 <= bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You have a normal weight")
elif 25 <= bmi < 30:
    print("You are overweight")
elif 30 <= bmi < 35:
    print("You're obese")
elif 35 <= bmi < 40:
    print("You're severely obese")
elif 40 <= bmi:
    print("You're morbidly obese")