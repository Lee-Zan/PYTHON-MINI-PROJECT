import random

print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'stop' anytime to quit.\n")

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper or scissors: ").lower()

    if user_choice == "stop":
        print("You stopped the game. Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!\n")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!\n")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!\n")
    else:
        print("You lose!\n")