print("Welcome to my calculator!")
num1 = float(input("Enter a number: "))
sign = input("+,-,* or/: ")
num2 = float(input("Enter another number: "))
if sign == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif sign == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif sign == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif sign == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("input again")
