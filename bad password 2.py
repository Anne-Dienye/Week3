#coding
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")

    if password1 != password2:
        print("Error: Passwords do not match. Try again.")
        continue

    if not (8 <= len(password1) <= 12):
        print("Error: Password must be between 8 and 12 characters. Try again.")
        continue

    if password1 in BAD_PASSWORDS:
        print("Error: Password is too common. Try again.")
        continue

    print("Password Set")
    break