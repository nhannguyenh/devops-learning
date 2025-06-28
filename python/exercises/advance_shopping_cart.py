foods = []
prices = []
total = 0

while True:
    food = input("Enter the food that you would like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for price in prices:
    total += price

print(f"The total price is ${total}")