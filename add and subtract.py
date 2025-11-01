def sum_numbers(first_number: int, second_number: int):
    return first_number + second_number

def subtract(some_result: int, third_number: int):
    return some_result - third_number


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = add_and_subtract(num1, num2, num3)
print(result)