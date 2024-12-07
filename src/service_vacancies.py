class Vacancies:
    """Класс для работы с вакансиями"""

    __list_vacancies = []
    __slots__ = ("__name", "__url", "__salary", "__responsibility", "__requirements")

    def __init__(
        self,
        name: str,
        url: str,
        salary: dict | str = "Зарплата не указана",
        responsibility: str = "Описание не указано",
        requirements: str = "Требования не указаны",
    ):
        """Конструктор класса"""

        self.__name = name
        self.__url = url
        self.__salary = self.__validate_salary(salary)
        self.__responsibility = responsibility
        self.__requirements = requirements
        dict_vacancy = {
            "name": self.__name,
            "url": self.__url,
            "salary": self.__salary,
            "responsibility": self.__responsibility,
            "requirements": self.requirements,
        }
        self.__list_vacancies.append(dict_vacancy)

    @classmethod
    def get_vacancies_from_list(cls, vacancies_list: list) -> list:
        """Получение вакансий из списка"""

        for vacancy in vacancies_list:
            url = vacancy.get("url") if vacancy.get("url") else vacancy.get("alternate_url")
            salary = cls.__validate_salary(vacancy.get("salary"))
            responsibility = vacancy["snippet"].get("responsibility", "Обязанности не указаны")
            requirements = vacancy["snippet"].get("requirements", "Требования не указаны")

            cls(
                name=vacancy.get("name", "Не указано"),
                url=url,
                salary=salary,
                responsibility=responsibility if responsibility is not None else "Не указано",
                requirements=requirements,
            )
        return cls.__list_vacancies

    @staticmethod
    def __validate_salary(salary: dict) -> dict:
        """Метод валидации зарплаты"""

        if salary is None or salary == "Зарплата не указана":
            return {"from": 0, "to": 0}
        else:
            return {
                "from": salary.get("from", "не указано"),
                "to": salary.get("to", "не указано"),
                "currency": salary.get("currency", "не указан"),
            }

    def __ge__(self, other) -> bool:
        """Метод сравнений вакансий по зарплате"""

        if self.__salary.get("to") is None or other.__salary.get("to") is None:
            return self.__salary.get("from") >= other.__salary.get("from")
        elif self.__salary.get("from") is None or other.__salary.get("from") is None:
            return self.__salary.get("to") >= other.__salary.get("to")
        else:
            avg_self_salary = (self.__salary.get("from") + self.__salary.get("to")) // 2
            avg_other_salary = (other.__salary.get("from") + other.__salary.get("to")) // 2
            return avg_self_salary >= avg_other_salary

    def __str__(self) -> str:
        return (
            f"{self.__name} - {self.__url}. Зарплата: {self.__salary}. Описание: {self.__responsibility}. "
            f"Требования: {self.__requirements}."
        )

    @classmethod
    def list_vacancies(cls):
        """Метод для получения всех вакансий"""

        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def responsibility(self):
        return self.__responsibility

    @property
    def requirements(self):
        return self.__requirements

