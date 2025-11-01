numbers = input().split()
rounded_list = []
def rounded_numbers(numbers):
    for num in numbers:
        rounded_list.append(round(float(num)))
    return rounded_list

print(rounded_numbers(numbers))
