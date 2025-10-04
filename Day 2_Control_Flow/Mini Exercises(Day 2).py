"""
Exercise 1: Grade Checker
Ask the user for marks (0–100).
If marks ≥ 90 → "Grade: A"
Else if marks ≥ 75 → "Grade: B"
Else if marks ≥ 50 → "Grade: C"
Else → "Grade: Fail"

👉 Hint: Use nested if inside one big if/elif ladder.
"""

marks = int(input("Enter your marks (0-100):"))

if marks >= 90:
    print("Grade:A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade:C")
else:
    print("Grade: Fail")


"""
Exercise 2: Even or Odd + Divisible by 5
Ask for a number.
First check if it’s even or odd.
Inside that check, also verify if it’s divisible by 5.

Example:
Input: 10 → "Even and divisible by 5"
Input: 7 → "Odd and not divisible by 5"
"""

number = int(input("Enter a number:"))

if number % 2 == 0:
    if number % 5 == 0:
        print("Even and divisible by 5")
else:
    print("Odd and not divisible by 5")

"""
Exercise 3: Login System
Ask for username and password.
If username is "admin"
Then check if password is "1234".
If yes → "Login successful!"
Else → "Wrong password."
Else → "No such user."
"""

username = input("Enter username:")
password = input("Enter password:")
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("No such user")


"""
Challenge 1: ATM Machine Simulation

Write a program that simulates a simple ATM.
The correct PIN is 1234.
Ask the user to enter a PIN.
If PIN is correct → show a menu:
Check Balance
Withdraw Money
Deposit Money
If PIN is wrong → show "Incorrect PIN. Try again."

👉 Extra rules:

Start with balance = 1000.
For withdraw: if amount > balance → "Insufficient funds".
For deposit: just add to balance.
Always print the updated balance after any transaction.
Hint: Use if for PIN check, then nested if/elif for the menu.
"""

balance = 1000
PIN = input("Enter a PIN code:")
if PIN == "1234":
    print("1. Check balance")
    print("2. Withdraw amount")
    print("3. Deposit amount")
    choice = int(input("Enter choice:"))

    if choice == 1:
        print(f"Your balance is: ${balance}")
    elif choice == 2:
        withdraw_amount = float(input("Enter amount to withdraw:"))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"Withdrawal successful! Your new balance is: ${balance}")
        else:
            print("Insufficient balance!")
    elif choice == 3:
        deposit_amount = float(input("Enter amount to deposit:"))
        balance += deposit_amount
        print(f"Deposit successful! Your new balance is: ${balance}")
    else:
        print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Try again.")

"""
Challenge 2: ATM Machine Simulation (Advanced)

Write a program that simulates a simple ATM machine.

Requirements:
The correct PIN is 1234.
Ask the user to enter a PIN.
If the PIN is wrong → show "Incorrect PIN. Try again."
Give the user only 3 attempts before the program exits.

If the PIN is correct → show a menu with options:
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit

Rules:
Start with balance = 1000.
For withdraw: if amount > balance → print "Insufficient funds".
For deposit: just add to balance.
Always print the updated balance after any transaction.

Keep showing the menu until the user chooses Exit.
"""

balance = 1000
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Login successful!\n")

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your balance is: ${balance}")

            elif choice == "2":
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Withdrawal successful! New balance: ${balance}")
                else:
                    print("Insufficient funds!")

            elif choice == "3":
                deposit_amount = float(input("Enter amount to deposit: "))
                balance += deposit_amount
                print(f"Deposit successful! New balance: ${balance}")

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        break

    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

        if attempts == 0:
            print("Too many failed attempts. Your card is blocked!")
