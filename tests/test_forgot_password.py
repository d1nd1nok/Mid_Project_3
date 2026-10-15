import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page()

        login_page.click_recover_password()

        forgot_page = ForgotPasswordPage(driver)
        assert forgot_page.is_opened(), "Не открылась страница восстановления пароля"



    @allure.title("Ввод почты и клик по кнопке «Восстановить» ведёт к вводу нового пароля")
    def test_submit_email_opens_reset_page(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page()

        forgot_page.submit_email(registered_user["email"])

        reset_page = ResetPasswordPage(driver)
        reset_page.wait_url_contains("reset-password")
        assert reset_page.is_opened(), "Не открылась страница ввода нового пароля"


    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле")
    def test_show_hide_password_highlights_field(self, driver, registered_user):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page()
        forgot_page.submit_email(registered_user["email"])

        reset_page = ResetPasswordPage(driver)
        reset_page.wait_url_contains("reset-password")

        reset_page.toggle_password_visibility()

        assert reset_page.wait_password_field_active(), (
            "Поле пароля должно подсветиться после клика по «глазику»"
        )
