from os import name

from src.hh_ru_api import HHApi
from src.file_json import JSONSaver
from src.utils import salary_difference
from src.service_vacancies import Vacancies


def service_connect() -> None:
    """Функция для взаимодействия с пользователем"""

    keyword = input("Введите поисковый запрос: ")
    print("Идёт поиск... ")
    hh = HHApi()
    vacancies = hh.load_vacancies(keyword)  # получаем вакансии
    vacancies = Vacancies.get_vacancies_from_list(vacancies)  # записываем вакансии в класс Vacancies
    data = JSONSaver()
    data.add_vacancy(vacancies)  # записываем данные в JSON файл
    top = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies = data.load_data()
    top_vacancies = sorted(
        vacancies, key=lambda x: x["salary"].get("to", 0) or 0, reverse=True
    )  # сортируем вакансии по зарплате
    print(f"Топ {top} вакансий по зарплате:")
    for i, vacancy in enumerate(top_vacancies[:top], start=1):
        print(f"{i}. {vacancy['name']} - Зарплата: от {vacancy['salary']["from"]} до {vacancy['salary']["to"]}")
    keyword = input("Введите ключевое слово для поиска вакансий ")
    filtered_vacancies = data.get_vacancies(keyword)
    for vacancy in filtered_vacancies:
        print(
            f"{vacancy["name"]} - Зарплата: от {vacancy['salary']["from"]} до {vacancy['salary']["to"]}. {vacancy["responsibility"]}. {vacancy["requirements"]}"
        )
    question = input("Желаете сравнить 2 вакансии по зарплате?(да/нет) ")
    if question.lower() == "да":
        name_1 = input("Укажите название первой вакансии ")
        name_2 = input("Укажите название второй вакансии ")
        result = salary_difference(vacancies, name_1, name_2)
        if result:
            print("Зарплата первой вакансии больше")
        else:
            print("Зарплата во второй вакансии больше")


if __name__ == "__main__":
    service_connect()