from selenium.webdriver.common.by import By


class AccountPageLocators:

    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    ORDER_CARD = (By.CSS_SELECTOR, "a[class*='OrderHistory_link']")
    ORDER_CARD_NUMBER = (By.CSS_SELECTOR, "p[class*='text_type_digits-default']")
