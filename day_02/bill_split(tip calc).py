print("Welcome to the Bill splitter (tip calculator)!")

total_bill = float(input(" what is the total bill?\n "))

tip = int(input("What percentage would you like to tip?\n "))

total_members = int(input(" How many members would you like to split the bill among?\n "))

tip_amount = total_bill * tip / 100

final_bill = total_bill + tip_amount

amount_per_person = final_bill / total_members

decimal = (input("Would you like to round off to the nearest rupee? YES or NO.\n "))
if decimal == "YES":
    print(f"Each person has to pay: ₹{round(amount_per_person)}")
else:
    print(f"Each person has to pay: ₹{round(amount_per_person, 2)}")

