from unittest.mock import mock_open, patch

from src.file_json import JSONSaver


@patch("builtins.open", new_callable=mock_open, read_data='[{"test1": "test", "test": "test"}]')
def test_load_data(mock_file):
    data = JSONSaver()
    assert data.load_data() == [{"test1": "test", "test": "test"}]


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "test", "responsibility": "somthing", "requirements": "тест"}]',
)
def test_get_vacancies(mock_file):
    data = JSONSaver()
    assert data.get_vacancies("test") == [{"name": "test", "responsibility": "somthing", "requirements": "тест"}]
    assert data.get_vacancies("Test") == [{"name": "test", "responsibility": "somthing", "requirements": "тест"}]
    assert data.get_vacancies("somthing") == [{"name": "test", "responsibility": "somthing", "requirements": "тест"}]
    assert data.get_vacancies("тест") == [{"name": "test", "responsibility": "somthing", "requirements": "тест"}]
    assert data.get_vacancies("not found") == []


def test_add_vacancy():
    data = JSONSaver("test")
    new_vacancy = [{"name": "test", "test": "test"}]
    data.add_vacancy(new_vacancy)
    assert len(data.load_data()) == 1
    data.add_vacancy(new_vacancy)
    assert len(data.load_data()) == 1
    second_vacancy = [{"name": "test", "responsibility": "somthing", "requirements": "тест"}]
    data.add_vacancy(second_vacancy)
    assert len(data.load_data()) == 2


def test_del_vacancy():
    data = JSONSaver("test")
    new_vacancy = [{"name": "test", "test": "test"}]
    data.add_vacancy(new_vacancy)
    data.del_vacancy("test")
    assert len(data.load_data()) == 0