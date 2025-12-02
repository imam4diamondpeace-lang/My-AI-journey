names = []
ages = []
favorites = []

for i in range(3):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    favorite = input("Enter your favorite: ")
    names.append(name)
    ages.append(age)
    favorites.append(favorite)
print("\n Here is the information you entered:")
for i in range(3):
    print(f"name: {names[i]}, age: {ages[i]}, favourite: {favorites[i]}")
total_age = 0
for age in ages:
    total_age += int(age)
average_age = total_age/len(ages)
print(f"The average age is {average_age}")
