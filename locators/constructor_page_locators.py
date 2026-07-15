from selenium.webdriver.common.by import By


class ConstructorPageLocators:

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

    COUNTER = (By.CSS_SELECTOR, "[class*='counter_counter__num']")
