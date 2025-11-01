def odd_even_sum(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for index in some_number:
        if index % 2 == 0:
            sum_of_even_digits += int(index)
        else:
            sum_of_odd_digits += int(index)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
number = input()
print(odd_even_sum(number))

def odd_even_sum(some_number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for index in some_number:
        digit = int(index)  # Преобразуваме символа в число

        if digit % 2 == 0:
            sum_of_even_digits += digit
        else:
            sum_of_odd_digits += digit

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

number = input()
print(odd_even_sum(number))