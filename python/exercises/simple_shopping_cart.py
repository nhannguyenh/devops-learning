item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quatity = int(input("How many would you like? "))

total = price + quatity
print(f"You have bought {quatity} {item}s")
print(f"Your total is ${total}")