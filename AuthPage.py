from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class AuthPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://trello.com/login"# адрес сайта
        self.__driver = driver

    def go(self):
        self.__driver.get(self.__url)

    def login_as(self, email: str, password: str ):
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email) # ввести локатор логина
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()# ввести локатор кнопки "продолжить"

        #дождаться появлени поля
        WebDriverWait(set.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))

        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password) # ввести локатор пароля
        self.__driver.find_element(By.CSS_SELECTOR, "#login-ыгиьше").click()# ввести локатор кнопки "ввод"

    def get_current_url(self):
        return self.__driver.current_url