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
