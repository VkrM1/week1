#generate 'n'number of terms in fibonacci

n = int(input("Enter the number of terms: "))

#2 terms
a, b = 0, 1  

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b