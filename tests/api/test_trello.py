import json
import os
import requests
import pytest
from dotenv import load_dotenv
import allure
from allure_commons.types import Severity
from utils.resource import schema_path
from jsonschema import validate
load_dotenv()

BASE_URL = 'https://api.trello.com'


@pytest.fixture
def board_id():
    url = f"{BASE_URL}/1/boards"
    params = {
        'name': 'Тестовая доска',
        'key': os.getenv('KEY'),
        'token': os.getenv('TOKEN')
    }

    response = requests.post(url, params=params)
    assert response.status_code == 200

    body = response.json()
    board_id = body.get('id')
    assert board_id is not None

    yield board_id


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Работа с trello")
@allure.story("Тестирование создания доски в trello")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_create_board(board_id):
    with allure.step('Проверяем что доска создана'):
        assert board_id is not None


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Работа с trello")
@allure.story("Тестирование обновления доски в trello")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_update_board(board_id):
    url = f"{BASE_URL}/1/boards/{board_id}"

    params = {
        'name': 'Обновленное имя доски',
        'key': os.getenv('KEY'),
        'token': os.getenv('TOKEN')
    }

    response = requests.put(url, params=params)

    with allure.step('Проверяем что статус кода == 200'):
        assert response.status_code == 200

    body = response.json()
    schema = schema_path('update_a_board_test.json')

    with allure.step('Проверяем что имя доски обновлено'):
        assert body.get('name') == 'Обновленное имя доски', "Имя доски не обновлено"
    with allure.step('Проверяем JSON schema'):
        with open(schema) as file:
            f = file.read()
            validate(body, schema=json.loads(f))


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Работа с trello")
@allure.story("Тестирование отображения информации о доске")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_get_board(board_id):
    url = f"{BASE_URL}/1/boards/{board_id}"
    params = {
        'key': os.getenv('KEY'),
        'token': os.getenv('TOKEN')
    }

    response = requests.get(url, params=params)

    with allure.step('Проверяем что статус кода == 200'):
        assert response.status_code == 200

@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Работа с trello")
@allure.story("Удаление доски")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_delete_board(board_id):
    url = f"{BASE_URL}/1/boards/{board_id}"
    params = {
        'key': os.getenv('KEY'),
        'token': os.getenv('TOKEN')
    }

    delete_response = requests.delete(url, params=params)

    with allure.step('Проверяем что статус кода удаления == 200'):
        assert delete_response.status_code == 200
