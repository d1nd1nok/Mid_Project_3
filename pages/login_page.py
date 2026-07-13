import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.urls import LOGIN_PAGE


class LoginPage(BasePage):

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    @allure.step("Открыть страницу входа")
    def open_page(self):
        self.open(LOGIN_PAGE)

    @allure.step("Авторизоваться пользователем {email}")
    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Кликнуть по ссылке «Восстановить пароль»")
    def click_recover_password(self):
        self.click(self.RECOVER_PASSWORD_LINK)

    @allure.step("Проверить, что открыта страница входа")
    def is_opened(self):
        return self.is_visible(self.LOGIN_BUTTON)
