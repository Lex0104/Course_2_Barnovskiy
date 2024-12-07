import json
import os

from src.file_api import BaseFile


class JSONSaver(BaseFile):
    """Класс для работы с файлом JSON"""

    def __init__(self, file_name: str = "json_vacancies.json"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_dir, f"../data/{file_name}.json")
        self.__file_name = os.path.abspath(path)
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_data(self) -> list:
        """Получение данных из файла"""

        with open(self.__file_name, encoding="utf-8") as file:
            json_data = json.load(file)
        return json_data

    def add_vacancy(self, vacancy_data: list) -> None:
        """Добавляет новую вакансию в файл"""

        with open(self.__file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            for vacancy in vacancy_data:
                if vacancy not in data:
                    data.append(vacancy)
        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

    def get_vacancies(self, keyword: str) -> list:
        """Возвращает вакансии по указанному критерию"""

        vacancy_filtered = []
        with open(self.__file_name, "r", encoding="utf-8") as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                name = vacancy.get("name", "")
                responsibility = vacancy.get("responsibility", "Обязанности не указаны")
                requirements = vacancy.get("requirements", "Требования не указаны")

                if (
                    keyword.lower() in name.lower()
                    or keyword.lower() in responsibility.lower()
                    or keyword.lower() in requirements.lower()
                ):
                    vacancy_filtered.append(vacancy)
            return vacancy_filtered

    def del_vacancy(self, name: str) -> None:
        """Удаляет вакансии по указанному имени"""

        new_vacancies = []
        with open(self.__file_name, "r+", encoding="utf-8") as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                if vacancy.get("name").lower() != name.lower():
                    new_vacancies.append(vacancy)
            file.seek(0)
            file.truncate()
            json.dump(new_vacancies, file, ensure_ascii=False, indent=4)
