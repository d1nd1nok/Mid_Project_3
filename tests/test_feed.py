import allure

from pages.feed_page import FeedPage
from src.api_helpers import ApiClient


@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Клик по заказу открывает всплывающее окно с деталями")
    def test_order_modal_opens(self, driver):
        feed = FeedPage(driver)
        feed.open_page()

        feed.open_first_order()

        assert feed.is_order_modal_opened(), "Не открылась модалка деталей заказа"



    @allure.title("Заказ пользователя отображается в общей ленте заказов")
    def test_user_order_appears_in_feed(self, driver, registered_user, ingredients):
        order_number = ApiClient.create_order(registered_user["access_token"], ingredients)

        feed = FeedPage(driver)
        feed.open_page()

        assert feed.wait_order_in_feed(order_number), (
            "Заказ пользователя не отобразился в ленте заказов"
        )




    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_counter_increases(self, driver, registered_user, ingredients):
        feed = FeedPage(driver)
        feed.open_page()
        total_before = feed.get_total_count()

        ApiClient.create_order(registered_user["access_token"], ingredients)

        assert feed.wait_total_count_above(total_before) > total_before, (
            "Счётчик «Выполнено за всё время» не увеличился"
        )

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(self, driver, registered_user, ingredients):
        feed = FeedPage(driver)
        feed.open_page()
        today_before = feed.get_today_count()

        ApiClient.create_order(registered_user["access_token"], ingredients)

        assert feed.wait_today_count_above(today_before) > today_before, (
            "Счётчик «Выполнено за сегодня» не увеличился"
        )

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_appears_in_progress(self, driver, registered_user, ingredients):
        feed = FeedPage(driver)
        feed.open_page()

        order_number = ApiClient.create_order(registered_user["access_token"], ingredients)

        feed.wait_order_in_progress(order_number)
        assert str(order_number).lstrip("0") in feed.get_in_progress_numbers(), (
            f"Заказ {order_number} не появился в разделе «В работе»"
        )




