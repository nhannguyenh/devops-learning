menus = {
    "Pizza": 3.00,
    "Nachos": 4.50,
    "Popcorn": 6.00,
    "Fries": 2.50,
    "Chips": 1.00,
    "Pretzel": 3.50,
    "Soda": 3.00,
    "Lemonade": 4.25
}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menus.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    if menus.get(food) is not None:
        cart.append(food)

print("---------- YOUR CART ----------")
for food in cart:
    total += menus.get(food)
    print(food, end=" ")

print()
print(f"Total is ${total:.2f}")