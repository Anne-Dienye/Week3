#coding
table_number = int(input("Enter the number for the times table (-12 to 12): "))
if -12 <= table_number <= 12:
    if table_number >= 0:
        for i in range(13):
            print(f"{i} x {table_number} = {i * table_number}")
    else:
        for i in range(12, -1, -1):
            print(f"{i} x {-table_number} = {i * -table_number}")
else:
    print("Error: Number must be between -12 and 12.")