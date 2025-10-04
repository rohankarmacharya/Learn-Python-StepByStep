# Exercise 1: Print numbers 1–10 using a for loop.

for i in range(1,11):
    print(i)

# Exercise 2: Print numbers 1–10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 3: Print only even numbers from 1–20 using continue.

for i in range(1,21):
    if i % 2 != 0:
        continue
    print(i)

# Exercise 4: Guessing game: keep asking for a number until the user enters 9.

while True:
    num = int(input("Guess a number:"))       
    if num == 9:
        print("You guessed it! Game Over.")
        break
    else:
        print("Please try again!")

'''
Exercise 5: 

Random Number Guessing Game

Task:
The computer picks a random number between 1 and 20.

The user keeps guessing until they find the correct number.

After each wrong guess, give a hint: "Too high!" or "Too low!".

When correct → "Correct! You guessed the number in X tries."
'''

import random  # Import the random module to generate random numbers

secret_number = random.randint(1,20)  # Generate a random integer between 1 and 20 (inclusive)
tries = 0  # Initialize a counter to keep track of how many guesses the user makes

while True:  # Start an infinite loop; it will keep asking the user until they guess correctly
    guess = int(input("Guess a number between 1 and 20:"))
    tries += 1      # Increase the guess counter by 1 for each attempt
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! You guessed the number in {tries} tries.")
        break  # Exit the loop since the correct number was guessed