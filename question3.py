#convert decimal to binary

# Get user input
decimal_number = int(input("Enter a decimal number: "))

if decimal_number < 0:
    print("Negative numbers cannot be converted to binary.")
else:
    binary_number = ""
    if decimal_number == 0:
        binary_number = "0"
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number //= 2
    print(f"The binary representation is: {binary_number}")
