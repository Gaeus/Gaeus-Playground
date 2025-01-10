Fahrenheit = input("Please typie in a temperature (F): ")
Celsius = (float(Fahrenheit) - 32) * 5.0/9.0
print(f"{Fahrenheit} degrees Fahrenheit equals {Celsius} degrees Celsius")
if Celsius < 0:
    print("Brr! It's cold in here!")
    