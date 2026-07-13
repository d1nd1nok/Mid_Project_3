import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):

    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    ORDER_CARD = (By.CSS_SELECTOR, "a[class*='OrderHistory_link']")
    ORDER_CARD_NUMBER = (By.CSS_SELECTOR, "p[class*='text_type_digits-default']")

    @allure.step("Проверить, что открыт личный кабинет (профиль)")
    def is_profile_opened(self):
        return self.is_visible(self.LOGOUT_BUTTON)

    @allure.step("Перейти в раздел «История заказов»")
    def open_order_history(self):
        self.click(self.ORDER_HISTORY_LINK)
        self.wait_visible(self.ORDER_CARD)

    @allure.step("Проверить, что открыта история заказов")
    def is_order_history_opened(self):
        return self.is_visible(self.ORDER_CARD)

    @allure.step("Получить номера заказов из истории")
    def get_order_numbers(self):
        numbers = []
        for card in self.find_all(self.ORDER_CARD):
            text = card.find_element(*self.ORDER_CARD_NUMBER).text.strip()
            numbers.append(text.lstrip("#").lstrip("0"))
        return numbers

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(self.LOGOUT_BUTTON)
