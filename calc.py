print("Ryan's Calculator")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter Second number: \n"))

print("Select an operator:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Division (/)")
print("4. Multiplication (*)")

operator = input("Enter operator(either the number or symbol):")

if operator == "1" or operator == "+":
    print(f"{num1} + {num2} =", num1 + num2)
elif operator == "2" or operator == "-":
    print(f"{num1} - {num2} =",num1 - num2)
elif operator == "3" or operator == "/":
    print(f"{num1} / {num2} =",num1 / num2)
elif operator == "4" or operator == "*":
    print(f"{num1} * {num2} =",num1 * num2)
else:
    print("Invalid input, please enter a valid operator")
