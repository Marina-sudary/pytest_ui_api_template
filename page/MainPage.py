import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from configuration.configProvider import configProvider

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = configProvider().get("ui", "base_url")
        self.__url = self.url+"/u/skyeng_user_d/boards"

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url
    
    @allure.step("Перейти на страницу авторизации")
    def gщ(self):
        self.__driver.get(self.__url)

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
    
    @allure.step("Добавит куки авторизации")
    def add_cookie(self):
        cookie = {
            "name": "token",
            "value": "kluch - token"
        }
        self.__driver.add_cookie(cookie)

    @allure.step("Нажать кнопку - Создать в шапке")    
    def open_creat_form(self):
        self.__driver.find_element(By.CSS_SELECTOR, "локатор кнопки").click()

    @allure.step("Выбрать {number} элемент в списке")
    def choose_option(self, number=1):
        popover = self.__driver.find_element(By.CSS_SELECTOR, "локатор элемента")
        lis = popover.find_element(By.CSS_SELECTOR, "li")
        lis[number-1].click()

    @allure.step("Указать имя новой доски = {board_name}")
    def fill_name(self, board_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "локатор элемента").send_keys(board_name)

    @allure.step("Нажать сохранить")
    def click_save_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, "локатор кнопки").click()
        WebDriverWait(self.__driver, 10).intil(EC.url_contains(self.url+"/b/"))