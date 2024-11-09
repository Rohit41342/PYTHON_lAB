 # WAP to print triangular  pattern

print("Pattern 1:")
for i in range(1, 5):  #  rows
    for j in range(i): # column
        print("*", end=" ") #printing 
    print()  # Move to the next line after each row


print("\nPattern 2:")
for i in range(1, 5):  #  rows
    for j in range(1, i + 1):   # column
        print(j, end=" ") #printing 
    print()  # Move to the next line after each row


print("Pattern 3:")
for i in range(1, 5):  #  rows
    for j in range(i):  # column
        print(i, end=" ") #printing 
    print()  # Move to the next line after each row
