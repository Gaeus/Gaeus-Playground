print("What's the weather forecast for tomorrow?")
temperature=float(input("Temperature:"))
rain=input("Will it rain tomorrow? (yes/no):").lower()
print("Wear jeans and a T-shirt")
if temperature<20:
  print("I recommend a jumper as well")
if temperature<10:
  print("Take a jacket with you")
if temperature<5:
    print("Make it a waarm coat, actually")
    print("I think gloves are in order")
if rain=="yes":
    print("Don't forget your umbrella")