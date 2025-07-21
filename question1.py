#program to input element into Array anf print all the elements.

# input element

def input_and_print_array():
    # Taking empty list
    array = []
    
    # Input number of elements
    n = int(input("Enter the number of elements you want to input: "))
    
    # Array input
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        array.append(element)
    
    # Print the array's element
    print("The elements in the array are:")
    for element in array:
        print(element)
# Function to input elements into an array and print them
def input_and_print_array():
    # Initialize an empty list
    array = []
    
    # Get the number of elements to input
    n = int(input("Enter the number of elements you want to input: "))
    
    # Input elements into the array
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        array.append(element)
    
    # Print all elements in the array
    print("The elements in the array are:")
    for element in array:
        print(element)

# Call the function
input_and_print_array()
