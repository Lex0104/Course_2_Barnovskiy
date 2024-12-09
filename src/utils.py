from src.service_vacancies import Vacancies


def salary_difference(vacancies: list, name_1: str, name_2: str) -> bool:
    """True, если зарплата первой вакансии больше"""

    vacancy_dict1 = {}
    vacancy_dict2 = {}

    for vacancy in vacancies:
        if name_1.lower() == vacancy["name"].lower():
            vacancy_dict1 = vacancy
            break

    for vacancy in vacancies:
        if name_2.lower() == vacancy["name"].lower() and vacancy != vacancy_dict1:
            vacancy_dict2 = vacancy
            break

    vacancy1 = Vacancies(**vacancy_dict1)
    vacancy2 = Vacancies(**vacancy_dict2)
    return vacancy1.__ge__(vacancy2)
