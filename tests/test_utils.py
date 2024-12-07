from src.utils import salary_difference


def test_compare_salaries():
    vacancies_list = [
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "Как-то",
            "requirements": "Что-то",
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 1, "to": 2, "currency": "RUB"},
            "responsibility": "разрабатывать",
            "requirements": "жив",
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru/",
            "salary": {"from": 4, "to": 5, "currency": "RUB"},
            "responsibility": "Обязанности не указаны",
            "requirements": "Требования не указаны",
        },
    ]
    assert (salary_difference(vacancies_list, "тестировщик", "Разработчик")) == True
    assert (salary_difference(vacancies_list, "Разработчик", "разработчик")) == False