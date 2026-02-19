import allure
from AuthPage import AuthPage
from MainPage import MainPage


def auth_test(browser):
    email = "mech694539@gmail.com"
    password = "Ch170169"
    username = "Marina"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = auth_page.get_current_url()
    with allure.step("Проверить, что URL + " + current_url + "skyeng_user_d/boards"):
        assert current_url.endswith("skyeng_user_d/boards") # проверь, что заканчивается вот такой подстрокой 
    
    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Проверить имя пользователя "+username):
            assert info [0] == username
        with allure.step("Проверить почту пользователя " +email):
            assert info[1]== email