numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum = 0
for i in numbers:
    if i is not None:
        sum += i

index = numbers.index(None)
numbers.remove(numbers[index])
numbers.insert(index, sum / (len(numbers) + 1))
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
