from AuthPage import AuthPage
from MainPage import MainPage


def auth_test(browser):
    email = "mech694539@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Ch170169")

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    assert auth_page.get_current_url().endswith("skyeng_user_d/boards") # проверь, что заканчивается вот такой подстрокой 
    assert info [0] == "Marina"
    assert info[1]== email