# WAP to get factorial of a number 

# Input number from the user
num = int(input("Enter a number: "))
factorial = 1

# Calculate factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Printing the result
print(f"The factorial of {num} is {factorial}")
