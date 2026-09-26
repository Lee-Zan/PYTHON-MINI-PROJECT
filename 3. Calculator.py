import math

print("\n-----Simple Calculator-----")
print("Type 'exit' anytime to quit.\n")

while True:
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root")
    print("6. Factorial")

    choice = input("Enter choice (1-6): ")

    if choice.lower() == "exit":
        print("Calculator closed")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!\n")
            continue

        if choice == "1":
            print("Result =", a + b)
        elif choice == "2":
            print("Result =", a - b)
        elif choice == "3":
            print("Result =", a * b)
        elif choice == "4":
            if b == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result =", a / b)

    elif choice in ["5", "6"]:
        try:
            a = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice == "5":
            print("Result =", math.sqrt(a))
        elif choice == "6":
            print("Result =", math.factorial(a))

    else:
        print("Invalid choice, please try again.")

    print()