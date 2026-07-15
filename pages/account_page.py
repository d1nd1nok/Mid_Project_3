import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):

    @allure.step("Проверить, что открыт личный кабинет (профиль)")
    def is_profile_opened(self):
        return self.is_visible(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Перейти в раздел «История заказов»")
    def open_order_history(self):
        self.click(AccountPageLocators.ORDER_HISTORY_LINK)
        self.wait_visible(AccountPageLocators.ORDER_CARD)

    @allure.step("Проверить, что открыта история заказов")
    def is_order_history_opened(self):
        return self.is_visible(AccountPageLocators.ORDER_CARD)

    @allure.step("Получить номера заказов из истории")
    def get_order_numbers(self):
        numbers = []
        for card in self.find_all(AccountPageLocators.ORDER_CARD):
            text = card.find_element(*AccountPageLocators.ORDER_CARD_NUMBER).text.strip()
            numbers.append(text.lstrip("#").lstrip("0"))
        return numbers

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
