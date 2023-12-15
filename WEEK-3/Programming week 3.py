# Qno.1
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
else:
    print("Hello, Stranger!")

# Qno.2
pass1 = input("Enter a new password: ")
pass2 = input("Confirm your password: ")
if pass1 == pass2:
    print("Password Sucessfully Set")
else:
    print("Error: Passwords do not match. Please try again.")

# Qno.3
pass1 = input("Enter a new password (between 8-12 character): ")
if 8 <= len(pass1) <= 12:
    pass2 = input("Confirm your password: ")
    if pass1 == pass2:
        print("Password Successfully Set!")
    else:
        print("Error: Passwords do not match. Please try again.")
else:
    print("Error: Password must be between 8 and 12 characters long.")

# Qno.4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
pass1 = input("Enter a new password (between 8-12 characters): ")
if 8 <= len(pass1) <= 12:
    if pass1 not in BAD_PASSWORDS:
        pass2 = input("Confirm your password: ")
        if pass1 == pass2:
            print("Password Successfully Set")
        else:
            print("Error: Passwords do not match. Please try again.")
    else:
        print("Error: Common password. Please choose a strong password.")
else:
    print("Error: Password must be between 8 and 12 characters long.")

# Qno.5
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    pass1 = input("Enter a new password ( between 8-12 characters): ")
    if 8 <= len(pass1) <= 12:
        if pass1 not in BAD_PASSWORDS:
            pass2 = input("Confirm your password: ")
            if pass1 == pass2:
                print("Password Successfully Set")
                break
            else:
                print("Error: Passwords do not match. Please try again.")
        else:
            print("Error: Common password. Please choose a strong password.")
    else:
        print("Error: Password must be between 8 and 12 characters long.")

# Qno.6
num = int(input("Enter a number: "))
for i in range(0, 13):
    print(f"{i} x {num} = {i*num}")

# Qno.7
num = int(input("Enter a number: "))
if num in range(0, 13):
    for i in range(0, 13):
        print(f"{i} x {num} = {i*num}")
else:
    print("Please enter a number between range 0-12")

# Qno.8
num = int(input("Enter a number: "))
if num < 0:
    for i in range(12, 0, -1):
        print(f"{i} x {num} = {i*num}")
else:
    for i in range(0, 13):
        print(f"{i} x {num} = {i*num}")