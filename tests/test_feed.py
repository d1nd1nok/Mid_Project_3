import allure

from pages.constructor_page import ConstructorPage
from pages.account_page import AccountPage
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



    @allure.title("Заказы пользователя из «Истории заказов» отображаются в ленте заказов")
    def test_user_order_appears_in_feed(self, logged_in_driver, registered_user):
        order_number = ApiClient.create_order(registered_user["access_token"])

        with allure.step("Заказ виден в истории заказов пользователя"):
            constructor = ConstructorPage(logged_in_driver)
            constructor.click_personal_account()
            account = AccountPage(logged_in_driver)
            account.open_order_history()
            assert str(order_number) in account.get_order_numbers(), (
                "Заказ не отобразился в истории заказов"
            )

        with allure.step("Тот же заказ виден в общей ленте заказов"):
            feed = FeedPage(logged_in_driver)
            feed.open_page()
            feed.wait_order_in_feed(order_number)




    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_counter_increases(self, driver, registered_user):
        feed = FeedPage(driver)
        feed.open_page()
        total_before = feed.get_total_count()

        ApiClient.create_order(registered_user["access_token"])

        assert feed.wait_total_count_above(total_before) > total_before, (
            "Счётчик «Выполнено за всё время» не увеличился"
        )

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases(self, driver, registered_user):
        feed = FeedPage(driver)
        feed.open_page()
        today_before = feed.get_today_count()

        ApiClient.create_order(registered_user["access_token"])

        assert feed.wait_today_count_above(today_before) > today_before, (
            "Счётчик «Выполнено за сегодня» не увеличился"
        )

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_appears_in_progress(self, driver, registered_user):
        feed = FeedPage(driver)
        feed.open_page()

        order_number = ApiClient.create_order(registered_user["access_token"])

        feed.wait_order_in_progress(order_number)
        assert str(order_number).lstrip("0") in feed.get_in_progress_numbers(), (
            f"Заказ {order_number} не появился в разделе «В работе»"
        )




