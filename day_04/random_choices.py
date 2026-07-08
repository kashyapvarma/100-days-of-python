import random
print("Welcome to the Game!")
user_choice = int(input("0 for rock, 1 for paper, 2 for scissors\n"))
computer_choice = random.randint(0,2)
choices = ["Rock", "Paper", "Scissors"]
print(f"Computer chose {choices[computer_choice]}")
if user_choice < 0 or user_choice > 2:
    print("Invalid input. You lose")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
else:
    print("You win!!")