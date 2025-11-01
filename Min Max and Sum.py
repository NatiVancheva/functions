numbers = input().split()
integer_list = [int(number) for number in numbers]
print(f"The minimum number is {min(integer_list)}")
print(f"The maximum number is {max(integer_list)}")
print(f"The sum number is: {sum(integer_list)}")