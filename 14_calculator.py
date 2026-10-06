first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("Cannot divide by zero")
        result = None
    else:
        result = first_number / second_number
else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result:", result)
