numbers = input()
def palindrome_numbers(numbers):
    num_list = [number for number in numbers.split(", ")]
    for number in num_list:
        print(number == number[::-1])
palindrome_numbers(numbers)