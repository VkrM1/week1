# Function to count positive and negative numbers

positive_count = 0
negative_count = 0

# Input the numbers
n = int(input("Enter the number of elements you want to input: "))

# Take input and count the positive and negative
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Print the counts
print(f"Number of positive numbers: {positive_count}")
print(f"Number of negative numbers: {negative_count}")
