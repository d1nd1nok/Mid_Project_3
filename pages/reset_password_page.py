import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    PASSWORD_FIELD_WRAPPER = (
        By.XPATH,
        "//div[contains(@class,'input_type_') and .//input[@name='Введите новый пароль']]",
    )
    SHOW_HIDE_ICON = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

    ACTIVE_FIELD_CLASS = "input_status_active"

    @allure.step("Проверить, что открыта страница ввода нового пароля")
    def is_opened(self):
        return self.is_visible(self.SAVE_BUTTON)

    @allure.step("Кликнуть по кнопке показать/скрыть пароль")
    def toggle_password_visibility(self):
        self.click(self.SHOW_HIDE_ICON)

    def _field_has_active_class(self):
        wrapper = self.wait_visible(self.PASSWORD_FIELD_WRAPPER)
        return self.ACTIVE_FIELD_CLASS in wrapper.get_attribute("class")

    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        return self._field_has_active_class()

    @allure.step("Дождаться, пока поле пароля станет активным (подсвеченным)")
    def wait_password_field_active(self, timeout=BasePage.DEFAULT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: self._field_has_active_class()
            )
            return True
        except Exception:
            return False
