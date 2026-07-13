import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.urls import MAIN_PAGE


class ConstructorPage(BasePage):

    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")
    BUNS_TAB = (By.XPATH, "//div[contains(@class,'tab') and .//span[text()='Булки']]")
    INGREDIENT = (By.CSS_SELECTOR, "a[class*='BurgerIngredient']")
    CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    INGREDIENT_MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal_opened']")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class*='Modal_modal__close']")

    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "[class*='Modal_modal_opened'] [class*='text_type_digits-large']",
    )

    _COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__num']")

    @allure.step("Открыть конструктор")
    def open_page(self):
        self.open(MAIN_PAGE)
        self.wait_visible(self.PAGE_TITLE)

    @allure.step("Проверить, что открыт конструктор")
    def is_opened(self):
        return self.is_visible(self.PAGE_TITLE)

    @allure.step("Кликнуть по первому ингредиенту")
    def open_ingredient_modal(self):
        self.click(self.INGREDIENT)

    @allure.step("Проверить, что открыта модалка деталей ингредиента")
    def is_ingredient_modal_opened(self):
        return self.is_visible(self.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрыть модалку по крестику")
    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модалка закрыта")
    def is_modal_closed(self):
        return self.wait_invisible(self.INGREDIENT_MODAL)

    def _ingredient_card(self, index=0):
        return self.find_all(self.INGREDIENT)[index]

    @allure.step("Получить значение счётчика ингредиента #{index}")
    def get_ingredient_counter(self, index=0):
        card = self._ingredient_card(index)
        value = card.find_element(*self._COUNTER).text.strip()
        return int(value) if value.isdigit() else 0

    @allure.step("Добавить ингредиент #{index} в заказ (перетаскиванием)")
    def add_ingredient_to_order(self, index=0):
        card = self._ingredient_card(index)
        basket = self.wait_visible(self.CONSTRUCTOR_BASKET)
        self.scroll_to(self.INGREDIENT)
        self.drag_and_drop(card, basket)

    @allure.step("Собрать бургер (булка + начинка)")
    def assemble_burger(self):
        self.add_ingredient_to_order(0)
        self.add_ingredient_to_order(5)

    @allure.step("Нажать «Оформить заказ»")
    def click_place_order(self):
        self.scroll_to(self.ORDER_BUTTON)
        self.click(self.ORDER_BUTTON)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        return self.wait_visible(self.ORDER_NUMBER, timeout=30).text.strip()
