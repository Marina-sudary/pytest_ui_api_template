import allure
import pytest
from pytest_ui_api_template.page.AuthPage import AuthPage
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.BoardApi import BoardApi

"https://trello.com/ru" 

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "token")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi("https://api.trello.com/1", "")

@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi("https://api.trello.com/1", "token")
    resp = api.create_board("Board to be deletede").get("id")
    return resp

@pytest.fixture
def delete_board()-> str:
    dictionary = {"board_id": ""}
    yield dictionary

    api = BoardApi("https://api.trello.com/1", "token")
    api.deletede_board_by_id(dictionary.get("board_id"))
  