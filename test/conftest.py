import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.remote.webdriver import WebDriver

from api.BoardApi import BoardApi
from configuration.configProvider import configProvider
from testdata.DataProvider import DataProvider

url = configProvider().get("api", "base_url")

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):

        timeout = configProvider().getint("ui", "timeout")
        browser_name = configProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


@pytest.fixture
def api_client() -> BoardApi:
    DataProvider().get_token()
    return BoardApi(
        configProvider().get("api", "base_url"), 
        DataProvider().get_token()
    )

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(configProvider().get("api", "base_url"), "")

@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi(
        configProvider().get("api", "base_url"),
        DataProvider().get_token()
    )

    with allure.step("Предварительно создать доску"):
        resp = api.create_board("Board to be deletede").get("id")

    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary

    with allure.step("Удалить ддоску после теста"):
        api = BoardApi(
            configProvider().get("api", "base_url"),
            DataProvider().get_token()
        )
        api.delete_board_by_id(dictionary.get("board_id"))

@pytest.fixture
def test_data():
    return DataProvider()
  