# 3seq.py

# Запрашиваем элементы первого списка у пользователя
input_string1 = input("Введите элементы 1-го списка через запятую: ")
list1 = [int(x.strip()) for x in input_string1.split(',')]

# Запрашиваем элементы второго списка у пользователя
input_string2 = input("Введите элементы 2-го списка через запятую: ")
list2 = [int(x.strip()) for x in input_string2.split(',')]

# Удаляем из первого списка элементы, присутствующие во втором списке
result_list = [x for x in list1 if x not in list2]

# Выводим результат
print("Результат:", result_list)
