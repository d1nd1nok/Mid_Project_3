import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from src.urls import FEED_PAGE


def _normalize(number):
    return str(number).lstrip("#").lstrip("0") or "0"


class FeedPage(BasePage):

    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")
    ORDER_CARD = (By.CSS_SELECTOR, "a[class*='OrderHistory_link']")
    ORDER_CARD_NUMBER = (By.CSS_SELECTOR, "p[class*='text_type_digits-default']")

    ORDER_MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal_opened']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class*='Modal_modal__close']")
    MODAL_ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "[class*='Modal_modal_opened'] [class*='text_type_digits']",
    )

    TOTAL_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    IN_PROGRESS_ITEMS = (By.CSS_SELECTOR, "ul[class*='orderListReady'] li")

    @allure.step("Открыть ленту заказов")
    def open_page(self):
        self.open(FEED_PAGE)
        self.wait_visible(self.ORDER_CARD)

    @allure.step("Проверить, что открыта лента заказов")
    def is_opened(self):
        return self.is_visible(self.PAGE_TITLE)

    @allure.step("Кликнуть по первому заказу в ленте")
    def open_first_order(self):
        self.click(self.ORDER_CARD)

    @allure.step("Проверить, что открыта модалка деталей заказа")
    def is_order_modal_opened(self):
        return self.is_visible(self.MODAL_ORDER_NUMBER)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_count(self):
        return int(self.get_text(self.TOTAL_COUNTER))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_count(self):
        return int(self.get_text(self.TODAY_COUNTER))

    @allure.step("Дождаться, пока «Выполнено за всё время» превысит {value}")
    def wait_total_count_above(self, value, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_total_count() > value
        )
        return self.get_total_count()

    @allure.step("Дождаться, пока «Выполнено за сегодня» превысит {value}")
    def wait_today_count_above(self, value, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_today_count() > value
        )
        return self.get_today_count()

    @allure.step("Получить номера заказов из ленты")
    def get_feed_order_numbers(self):
        numbers = []
        for card in self.find_all(self.ORDER_CARD):
            numbers.append(_normalize(card.find_element(*self.ORDER_CARD_NUMBER).text))
        return numbers

    @allure.step("Получить номера заказов из раздела «В работе»")
    def get_in_progress_numbers(self):
        numbers = []
        for item in self.driver.find_elements(*self.IN_PROGRESS_ITEMS):
            text = item.text.strip()
            if text and any(ch.isdigit() for ch in text):
                numbers.append(_normalize(text))
        return numbers

    @allure.step("Дождаться заказа {number} в разделе «В работе»")
    def wait_order_in_progress(self, number, timeout=30):
        target = _normalize(number)
        return WebDriverWait(self.driver, timeout).until(
            lambda d: target in self.get_in_progress_numbers()
        )

    @allure.step("Дождаться заказа {number} в ленте заказов")
    def wait_order_in_feed(self, number, timeout=30):
        target = _normalize(number)
        return WebDriverWait(self.driver, timeout).until(
            lambda d: target in self.get_feed_order_numbers()
        )
