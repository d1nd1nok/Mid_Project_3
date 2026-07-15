import allure

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from src.urls import FEED_PAGE


class FeedPage(BasePage):

    @staticmethod
    def _normalize(number):
        return str(number).lstrip("#").lstrip("0") or "0"

    @allure.step("Открыть ленту заказов")
    def open_page(self):
        self.open(FEED_PAGE)
        self.wait_visible(FeedPageLocators.ORDER_CARD)

    @allure.step("Проверить, что открыта лента заказов")
    def is_opened(self):
        return self.is_visible(FeedPageLocators.PAGE_TITLE)

    @allure.step("Кликнуть по первому заказу в ленте")
    def open_first_order(self):
        self.click(FeedPageLocators.ORDER_CARD)

    @allure.step("Проверить, что открыта модалка деталей заказа")
    def is_order_modal_opened(self):
        return self.is_visible(FeedPageLocators.MODAL_ORDER_NUMBER)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_count(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COUNTER))

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_count(self):
        return int(self.get_text(FeedPageLocators.TODAY_COUNTER))

    @allure.step("Дождаться, пока «Выполнено за всё время» превысит {value}")
    def wait_total_count_above(self, value, timeout=30):
        self.wait_until(lambda d: self.get_total_count() > value, timeout)
        return self.get_total_count()

    @allure.step("Дождаться, пока «Выполнено за сегодня» превысит {value}")
    def wait_today_count_above(self, value, timeout=30):
        self.wait_until(lambda d: self.get_today_count() > value, timeout)
        return self.get_today_count()

    @allure.step("Получить номера заказов из ленты")
    def get_feed_order_numbers(self):
        numbers = []
        for card in self.find_all(FeedPageLocators.ORDER_CARD):
            numbers.append(self._normalize(card.find_element(*FeedPageLocators.ORDER_CARD_NUMBER).text))
        return numbers

    @allure.step("Получить номера заказов из раздела «В работе»")
    def get_in_progress_numbers(self):
        numbers = []
        for item in self.find_elements(FeedPageLocators.IN_PROGRESS_ITEMS):
            text = item.text.strip()
            if text and any(ch.isdigit() for ch in text):
                numbers.append(self._normalize(text))
        return numbers

    @allure.step("Дождаться заказа {number} в разделе «В работе»")
    def wait_order_in_progress(self, number, timeout=30):
        target = self._normalize(number)
        return self.wait_until(
            lambda d: target in self.get_in_progress_numbers(), timeout
        )

    @allure.step("Дождаться заказа {number} в ленте заказов")
    def wait_order_in_feed(self, number, timeout=30):
        target = self._normalize(number)
        return self.wait_until(
            lambda d: target in self.get_feed_order_numbers(), timeout
        )
