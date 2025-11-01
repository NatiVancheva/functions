from urllib.parse import ParseResult

operator = input()
num1 = int(input())
num2 = int(input())
def calculate_numbers(a, b, operation):
    result = None
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b != 0:
            result = int(a / b)
    return result

print(calculate_numbers(num1, num2, operator))

def calculate_result(num1, num2, operator):
    return {
        "multiply": num1 + num2,
        "divide": int(num1 / num2),
        "add": num1 + num2,
        "subtract": num1 - num2
    }.get(operator, "Invalid operator")

operator = input("Enter the operator (multiply, divide, add, subtract")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = calculate_result(num1, num2, operator)
print(f"Result: {result}")