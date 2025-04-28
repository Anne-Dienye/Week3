#coding
name = input("Hello, what is your name? ").strip()
if not name:
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}. Good to meet you!")