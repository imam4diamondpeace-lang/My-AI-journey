grocery_list = []
for i in range(3):
    item = input("Enter an item for your grocery list: ")
    grocery_list.append(item)
print("\nYour grocery list:")
for item in grocery_list:
    print("-", item)