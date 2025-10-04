"""
Exercise 1. Write a program that asks for your name and age, then print a message:
Hello {name}, you will be {age+2} in 2 years!
"""

name = input("Enter your name:")
age = int(input("Enter your age:"))

print(f"Hello {name}, you will be {age + 2} in 2 years!")

# tweak
name = input("Enter your name:")
age = int(input("Enter your age:"))
years_ahead = int(input("How many years to look ahead?"))
future_age = age + years_ahead
print(f"Hello {name}, you will be {future_age} in  {years_ahead} years!")


"""
Exercise 2: Write a program that asks the user for two numbers.

The program should calculate and print:

- Sum
- Difference
- Product
- Quotient (if the second number is not zero)
- Floor Division (if the second number is not zero)
- Remainder (if the second number is not zero)

If the second number is zero, print:

`"Cannot divide by zero"`
"""

a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")

if b != 0:
    print(f"Quotient: {a / b}")
    print(f"Floor Division: {a // b}")
    print(f"Remainder: {a % b}")
else:
    print("Cannot divide by zero")

"""
Exercise 3:
Write a program that converts a temperature in Celsius → Fahrenheit.
"""

celsius = float(input("Enter a degree in celsius:"))
fahrenheit = (celsius * 9 / 5) + 32  # formula
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
# :.2f is a format specifier inside an f-string.
# : → tells Python we’re applying formatting rules
# .2 → means 2 decimal places
# f → means floating-point number
