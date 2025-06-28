import random

number = random.randint(1, 6)
print(number)

floatNumber = random.random()
print(f"{floatNumber:.2f}")

options = ("rock", "paper", "scissors")
print(random.choice(options))