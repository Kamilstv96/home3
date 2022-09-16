element = int(input('Введите количество элементов'))
result =[]
for i in range(element):
    number = int(input('Введите число'))
    result.append(number)
result.sort()
print(result)
