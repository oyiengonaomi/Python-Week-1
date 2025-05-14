# Simple Calculator

# Get user input
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Initialize result variable
result = None

# Perform the operation
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Cannot divide by zero."
else:
    result = "Error: Invalid operation."

# Display the result
if isinstance(result, str):
    print(result)
else:
    print(f"{first_number} {operation} {second_number} = {result}")
