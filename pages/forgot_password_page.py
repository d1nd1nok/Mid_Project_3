import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.urls import FORGOT_PASSWORD_PAGE


class ForgotPasswordPage(BasePage):

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

    @allure.step("Открыть страницу восстановления пароля")
    def open_page(self):
        self.open(FORGOT_PASSWORD_PAGE)

    @allure.step("Ввести email и нажать «Восстановить»")
    def submit_email(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.RECOVER_BUTTON)

    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_opened(self):
        return self.is_visible(self.RECOVER_BUTTON)
