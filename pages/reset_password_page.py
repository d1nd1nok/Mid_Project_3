import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    @allure.step("Проверить, что открыта страница ввода нового пароля")
    def is_opened(self):
        return self.is_visible(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step("Кликнуть по кнопке показать/скрыть пароль")
    def toggle_password_visibility(self):
        self.click(ResetPasswordPageLocators.SHOW_HIDE_ICON)

    def _field_has_active_class(self):
        wrapper = self.wait_visible(ResetPasswordPageLocators.PASSWORD_FIELD_WRAPPER)
        return ResetPasswordPageLocators.ACTIVE_FIELD_CLASS in wrapper.get_attribute("class")

    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self):
        return self._field_has_active_class()

    @allure.step("Дождаться, пока поле пароля станет активным (подсвеченным)")
    def wait_password_field_active(self, timeout=BasePage.DEFAULT_TIMEOUT):
        try:
            self.wait_until(lambda d: self._field_has_active_class(), timeout)
            return True
        except Exception:
            return False
