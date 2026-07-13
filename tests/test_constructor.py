import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from src.urls import FEED_PAGE, MAIN_PAGE


@allure.epic("Stellar Burgers UI")
@allure.feature("Основной функционал (конструктор)")
class TestConstructor:

    @allure.title("Переход в конструктор по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        feed = FeedPage(driver)
        feed.open_page()

        constructor = ConstructorPage(driver)
        constructor.click_constructor()

        constructor.wait_url_to_be(MAIN_PAGE)
        assert constructor.is_opened(), "Не открылся конструктор"

    @allure.title("Переход в ленту заказов по клику на «Лента Заказов»")
    def test_go_to_order_feed(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open_page()

        constructor.click_order_feed()

        constructor.wait_url_to_be(FEED_PAGE)
        feed = FeedPage(driver)
        assert feed.is_opened(), "Не открылась лента заказов"

    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open_page()

        constructor.open_ingredient_modal()

        assert constructor.is_ingredient_modal_opened(), (
            "Не открылась модалка деталей ингредиента"
        )

    @allure.title("Всплывающее окно ингредиента закрывается по крестику")
    def test_ingredient_modal_closes(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open_page()
        constructor.open_ingredient_modal()
        assert constructor.is_ingredient_modal_opened()

        constructor.close_modal()

        assert constructor.is_modal_closed(), "Модалка не закрылась по крестику"

    @allure.title("При добавлении ингредиента в заказ увеличивается его счётчик")
    def test_ingredient_counter_increases(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open_page()

        counter_before = constructor.get_ingredient_counter(0)
        constructor.add_ingredient_to_order(0)
        counter_after = constructor.get_ingredient_counter(0)

        assert counter_after > counter_before, (
            f"Счётчик ингредиента не увеличился: было {counter_before}, стало {counter_after}"
        )

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, logged_in_driver):
        constructor = ConstructorPage(logged_in_driver)
        constructor.assemble_burger()

        constructor.click_place_order()

        order_number = constructor.get_order_number()
        assert order_number.isdigit(), (
            f"Не отобразился номер оформленного заказа: {order_number!r}"
        )
