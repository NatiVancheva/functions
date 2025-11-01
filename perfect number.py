number = int(input())
def perfect_number(number):
    divisor = [i for i in range(1, number) if number % i == 0]
    sum_divisor = sum(divisor)
    if sum_divisor == number:
       return "We have a perfect number!"
    return "It's not so perfect."
print(perfect_number(number))


divisor_sum = 0
for divisor in range(1, number):
    if number % divisor == 0:
        divisor_sum += divisor