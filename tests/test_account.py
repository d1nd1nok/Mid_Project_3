import allure

from pages.constructor_page import ConstructorPage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from src.api_helpers import ApiClient
from src.urls import PROFILE_PAGE, ORDER_HISTORY_PAGE


@allure.epic("Stellar Burgers UI")
@allure.feature("Личный кабинет")
class TestAccount:

    @allure.title("Переход в личный кабинет по клику на «Личный Кабинет»")
    def test_open_personal_account(self, logged_in_driver):
        constructor = ConstructorPage(logged_in_driver)
        constructor.click_personal_account()

        constructor.wait_url_to_be(PROFILE_PAGE)
        account = AccountPage(logged_in_driver)
        assert account.is_profile_opened(), "Не открылся личный кабинет"

    @allure.title("Переход в раздел «История заказов»")
    def test_open_order_history(self, logged_in_driver, registered_user, ingredients):
        ApiClient.create_order(registered_user["access_token"], ingredients)

        constructor = ConstructorPage(logged_in_driver)
        constructor.click_personal_account()

        account = AccountPage(logged_in_driver)
        account.open_order_history()

        constructor.wait_url_to_be(ORDER_HISTORY_PAGE)
        assert account.is_order_history_opened(), "Не открылась история заказов"

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_driver):
        constructor = ConstructorPage(logged_in_driver)
        constructor.click_personal_account()

        account = AccountPage(logged_in_driver)
        account.logout()

        login_page = LoginPage(logged_in_driver)
        login_page.wait_url_contains("login")
        assert login_page.is_opened(), "После выхода не открылась страница входа"
