import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from src.urls import LOGIN_PAGE


class LoginPage(BasePage):

    @allure.step("Открыть страницу входа")
    def open_page(self):
        self.open(LOGIN_PAGE)

    @allure.step("Авторизоваться пользователем {email}")
    def login(self, email, password):
        self.type(LoginPageLocators.EMAIL_INPUT, email)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть по ссылке «Восстановить пароль»")
    def click_recover_password(self):
        self.click(LoginPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step("Проверить, что открыта страница входа")
    def is_opened(self):
        return self.is_visible(LoginPageLocators.LOGIN_BUTTON)
