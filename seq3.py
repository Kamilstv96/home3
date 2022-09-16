str_number = input('Введите числа через запятую')
numbers = str_number.split(',')

str_number = input('Введите числа через запятую')
second_numbers = str_number.split(',')

print(numbers)
print(second_numbers)

for number in numbers[:]:
    if number in second_numbers:
        numbers.remove(number)
print(numbers)
