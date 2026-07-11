import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',]

n_letters = int(input("How many letters would you like?"))
n_numbers = int(input("How many numbers would you like?"))
n_symbols = int(input("How many symbols would you like?"))

password = []
for i in range(n_letters):
    password += random.choice(letters)
for j in range(n_numbers):
    password += random.choice(numbers)
for k in range(n_symbols):
    password += random.choice(symbols)

random.shuffle(password)
final_password = "".join(password)
print(final_password)