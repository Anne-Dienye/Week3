#coding
table_number = int(input("Enter the number for the times table (0-12): "))
if 0 <= table_number <= 12:
    for i in range(13):
        print(f"{i} x {table_number} = {i * table_number}")
else:
    print("Error: Number must be between 0 and 12.")