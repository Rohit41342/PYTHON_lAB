# Using input function take two number and then swap

# Take two number as input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Now Swap the numbers
temp1 = a
a = b
b = temp1

#printing the number
print("Swap number: ",a,b)