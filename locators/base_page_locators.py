from selenium.webdriver.common.by import By


class BasePageLocators:

    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_LINK = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo'] a")
