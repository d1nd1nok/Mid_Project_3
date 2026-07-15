import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from src.urls import FORGOT_PASSWORD_PAGE


class ForgotPasswordPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open_page(self):
        self.open(FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести email и нажать «Восстановить»")
    def submit_email(self, email):
        self.type(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_opened(self):
        return self.is_visible(ForgotPasswordPageLocators.RECOVER_BUTTON)
