def is_even(number: int):
    return number % 2 == 0
numbers_as_string = input().split()
result = []
for current_number in numbers_as_string:
    if is_even(int(current_number)):
        result.append(int(current_number))
#numbers_as_digits = []
#for number in numbers_as_string:
    #numbers_as_digits.append(int(number))
#result = list(filter(is_even, numbers_as_digits))
print(result)


