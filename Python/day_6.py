questions = [
    {"q": "2 + 2 = ", "a": "4"},
    {"q": "3 * 3 = ", "a": "9"},
    {"q": "5 - 1 = ", "a": "4"}
]

score = 0

for item in questions:
    answer = input(item["q"] + " ")
    if answer == item["a"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your total score is:", score, "out of", len(questions))
