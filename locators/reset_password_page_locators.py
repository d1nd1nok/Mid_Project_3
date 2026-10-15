from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    PASSWORD_FIELD_WRAPPER = (
        By.XPATH,
        "//div[contains(@class,'input_type_') and .//input[@name='Введите новый пароль']]",
    )
    SHOW_HIDE_ICON = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")

    ACTIVE_FIELD_CLASS = "input_status_active"
