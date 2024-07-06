# victory.py

import random

# Данные о знаменитостях
celebrities = {
    "А.С. Пушкин": "06.06.1799",
    "Л.Н. Толстой": "09.09.1828",
    "Ф.М. Достоевский": "11.11.1821",
    "И.С. Тургенев": "09.11.1818",
    "М.Ю. Лермонтов": "15.10.1814",
    "С.А. Есенин": "03.10.1895",
    "А.А. Ахматова": "23.06.1889",
    "В.В. Маяковский": "19.07.1893",
    "Н.А. Некрасов": "10.12.1821",
    "И.А. Бунин": "22.10.1870"
}


def format_date(date_str):
    """Форматирует дату 'dd.mm.yyyy' в 'd mmmm yyyy года'"""
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    day, month, year = date_str.split('.')
    return f"{int(day)} {months[int(month) - 1]} {year} года"


def quiz():
    # Выбираем 5 случайных знаменитостей
    selected_celebrities = random.sample(list(celebrities.items()), 5)

    correct_answers = 0

    # Спрашиваем пользователя
    for name, correct_date in selected_celebrities:
        user_date = input(f"Введите дату рождения {name} (дд.мм.гггг): ")
        if user_date == correct_date:
            correct_answers += 1
        else:
            formatted_date = format_date(correct_date)
            print(f"Неверно. Правильный ответ: {formatted_date}")

    # Подсчет и вывод результатов
    total_questions = len(selected_celebrities)
    incorrect_answers = total_questions - correct_answers
    correct_percentage = (correct_answers / total_questions) * 100
    incorrect_percentage = 100 - correct_percentage

    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {incorrect_answers}")
    print(f"Процент правильных ответов: {correct_percentage:.2f}%")
    print(f"Процент неправильных ответов: {incorrect_percentage:.2f}%")

    # Предлагаем начать заново
    restart = input("Хотите начать игру сначала? (да/нет): ").strip().lower()
    if restart == 'да':
        quiz()


# Запуск викторины
if __name__ == "__main__":
    quiz()
