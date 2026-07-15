import allure

from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from src.urls import MAIN_PAGE


class ConstructorPage(BasePage):

    @allure.step("Открыть конструктор")
    def open_page(self):
        self.open(MAIN_PAGE)
        self.wait_visible(ConstructorPageLocators.PAGE_TITLE)

    @allure.step("Проверить, что открыт конструктор")
    def is_opened(self):
        return self.is_visible(ConstructorPageLocators.PAGE_TITLE)

    @allure.step("Кликнуть по первому ингредиенту")
    def open_ingredient_modal(self):
        self.click(ConstructorPageLocators.INGREDIENT)

    @allure.step("Проверить, что открыта модалка деталей ингредиента")
    def is_ingredient_modal_opened(self):
        return self.is_visible(ConstructorPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть модалку по крестику")
    def close_modal(self):
        self.click(ConstructorPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модалка закрыта")
    def is_modal_closed(self):
        return self.wait_invisible(ConstructorPageLocators.INGREDIENT_MODAL)

    def _ingredient_card(self, index=0):
        return self.find_all(ConstructorPageLocators.INGREDIENT)[index]

    @allure.step("Получить значение счётчика ингредиента #{index}")
    def get_ingredient_counter(self, index=0):
        card = self._ingredient_card(index)
        value = card.find_element(*ConstructorPageLocators.COUNTER).text.strip()
        return int(value) if value.isdigit() else 0

    @allure.step("Добавить ингредиент #{index} в заказ (перетаскиванием)")
    def add_ingredient_to_order(self, index=0):
        card = self._ingredient_card(index)
        basket = self.wait_visible(ConstructorPageLocators.CONSTRUCTOR_BASKET)
        self.scroll_to(ConstructorPageLocators.INGREDIENT)
        self.drag_and_drop(card, basket)

    @allure.step("Собрать бургер (булка + начинка)")
    def assemble_burger(self):
        self.add_ingredient_to_order(0)
        self.add_ingredient_to_order(5)

    @allure.step("Нажать «Оформить заказ»")
    def click_place_order(self):
        self.scroll_to(ConstructorPageLocators.ORDER_BUTTON)
        self.click(ConstructorPageLocators.ORDER_BUTTON)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        return self.wait_visible(ConstructorPageLocators.ORDER_NUMBER, timeout=30).text.strip()
