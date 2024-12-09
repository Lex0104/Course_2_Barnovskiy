from abc import ABC, abstractmethod


class BaseFile(ABC):
    """Абстрактный класс для работы с файлом"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    @abstractmethod
    def del_vacancy(self, name):
        pass
