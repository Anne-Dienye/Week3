#coding
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter a new password: ")
password2 = input("Re-enter the password: ")

if password1 == password2:
    if 8 <= len(password1) <= 12:
        if password1 not in BAD_PASSWORDS:
            print("Password Set")
        else:
            print("Error: Password is too common.")
    else:
        print("Error: Password must be between 8 and 12 characters.")
else:
    print("Error: Passwords do not match.")