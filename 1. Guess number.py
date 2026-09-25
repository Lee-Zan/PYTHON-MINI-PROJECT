import random

target = random.randint(1, 100)

print("------- The Guessing Challenge -------")

while True:
    userChoice = input("Guess the Number (1-100) or type 'Quit': ")

    if userChoice.lower() == "quit":
        print("You quit the game...")
        break

    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid input! Please enter a number or 'Quit'.")
        continue

    if userChoice == target:
        print("You got it, Correct Guess!!")
        break
    elif userChoice < target:
        print("Your number was too small. Try a bigger guess...")
    else:
        print("Your number was too big. Try a smaller guess...")

print("--- Game Over ---")