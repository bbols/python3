# 2seq.py

# Запрашиваем элементы у пользователя
input_string = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Определяем разделитель
if ',' in input_string:
    separator = ','
elif ';' in input_string:
    separator = ';'
elif '/' in input_string:
    separator = '/'
else:
    print("Неправильный ввод!")
    exit(1)

# Разделяем строку на элементы
elements = [int(x.strip()) for x in input_string.split(separator)]

# Находим уникальные элементы
unique_elements = [x for x in elements if elements.count(x) == 1]

# Выводим уникальные элементы
print("Результат:", unique_elements)
