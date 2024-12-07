from unittest.mock import patch

from src.hh_ru_api import HHApi


def test_init_hh_api():
    hh_api = HHApi("/Users/eduardmaksimovicbarnovskij/work/temp/Course_2_Barnovskiy/data/vacancies.json")
    assert hh_api.file_worker == "/Users/eduardmaksimovicbarnovskij/work/temp/Course_2_Barnovskiy/data/vacancies.json"


@patch("requests.get")
def test_load_vacancies(mock_convert):
    hh_api = HHApi("/Users/eduardmaksimovicbarnovskij/work/temp/Course_2_Barnovskiy/data/vacancies.json")
    mock_convert.return_value.json.return_value = {"items": [{"test1": "test1"}]}
    assert hh_api.load_vacancies("Python") == [
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
        {"test1": "test1"},
    ]