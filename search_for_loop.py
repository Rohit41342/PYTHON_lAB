# WAP to traverse a list of item and find particular item is present in the list or not

# list of items
items = ["apple", "banana", "cherry", "date", "elderberry"]

# Taking input from user for search the Item.
search_item = input("Enter the item to search for: ")

# Traverse the list to find the item
for item in items:
    if item == search_item:
        print(f"{search_item} is present in your list.")
        break
else:
    # This 'else' block runs if the item is not found in the list
    print(f"{search_item} is not present in your list.")
