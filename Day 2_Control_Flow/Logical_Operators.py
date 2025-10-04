# and → both must be true
# or → at least one true
#not → flips True/False


age = 19
has_id = True

if age>=18 and has_id:
    print("You can enter")
else:
    print("You can't. Access denied")


age = 19
has_id = False

if age>=18 or has_id:
    print("You can enter")
else:
    print("You can't. Access denied")


is_logged_in = False

if not is_logged_in:
    print("You must login first!")
else:
    print("You are welcome!")

# and, or and not altogether
username = "rohan"
password = "makechesterf*ckingproud"
is_subscribed = False

if username == "rohan" and password == "makechesterf*ckingproud":
    if not is_subscribed:
        print("Login successful but you are not subscribed.")
    else:
        print("Login successful and you are subscribed.")
else:
    print("Invalid username or password!")

login_input = "rohankarmacharya9@gmail.com"
if login_input =="rohan" or login_input=="rohankarmacharya9@gmail.com":
    print("Valid login input")



# Nested if
age = int(input("Enter your age:"))

if age>=18:
    has_license = input("Do you have a driving license? (yes/no):").lower()
    if has_license =="yes":
        print("You are allowed to drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too youung to drive, sorry.")