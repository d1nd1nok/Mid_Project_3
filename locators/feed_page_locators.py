from selenium.webdriver.common.by import By


class FeedPageLocators:

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
