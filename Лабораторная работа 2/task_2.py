# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

result = []

for first in participants_first_group.split("|"):
    if first in participants_second_group:
        result.append(first)
print(result)