print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")

bill = 0

if size == "S":
    bill += 250
elif size == "M":
    bill += 400
elif size == "L":
    bill += 500
else:
    print("Invalid pizza size.")

pepperoni = input("Do you want pepperoni? Y or N: ")

if pepperoni == "Y":
    if size == "S":
        bill += 50
    else:
        bill += 100

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 100

print(f"Your final bill is: ${bill}")