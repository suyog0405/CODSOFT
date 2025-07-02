print("========== CODSOFT CALCULATOR ==========")

print("Choose operation:")
print("1 -> Addition")
print("2 -> Subtraction")
print("3 -> Multiplication")
print("4 -> Division")

operation = input("Enter your choice (1/2/3/4): ")

# Take input numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid number input. Please enter numeric values only.")1
    exit()

# Perform operation
if operation == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == '3':
    result = num1 * num2
    print(f"Result: {num1} × {num2} = {result}")

elif operation == '4':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"Result: {num1} ÷ {num2} = {round(result, 2)}")

else:
    print("Invalid choice. Please select from 1 to 4.")