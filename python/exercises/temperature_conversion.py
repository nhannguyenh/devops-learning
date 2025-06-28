unit = input("Is this temperature in Celsius (C) or Fahenheit (F)? ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((temperature * 9 / 5) + 32, 1)
    print(f"The temperature in Fahenheit is {temperature}°F")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is {temperature}°C")
else:
    print(f"{unit} is an invalid unit of measurement")