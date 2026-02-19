import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url

    @allure.step("Открыть боковое окно")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click() # кнопка меню в правом углу

    @allure.step("Прочитать информацию о пользователе")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR,"div[data-testid=account-menu]>div>div:account-section]")
        fields = container.find_element(By.CSS_SELECTOR, 'div')
        name = fields[0].text
        email = fields[1].text
    # Возвращаем имя и почту пользователя:
        return [name, email]
