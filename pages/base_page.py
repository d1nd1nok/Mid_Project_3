import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Симуляция HTML5 drag-and-drop через JS: react-dnd слушает нативные
# drag-события, которые ActionChains не всегда воспроизводит в Firefox.
_HTML5_DND_SCRIPT = """
const source = arguments[0], target = arguments[1];
const dt = new DataTransfer();
const rect = target.getBoundingClientRect();
const opts = {bubbles: true, cancelable: true, dataTransfer: dt,
  clientX: rect.left + rect.width / 2, clientY: rect.top + rect.height / 2};
source.dispatchEvent(new DragEvent('dragstart', opts));
target.dispatchEvent(new DragEvent('dragenter', opts));
target.dispatchEvent(new DragEvent('dragover', opts));
target.dispatchEvent(new DragEvent('drop', opts));
source.dispatchEvent(new DragEvent('dragend', opts));
"""


class BasePage:

    DEFAULT_TIMEOUT = 15

    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_LINK = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo'] a")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться URL {url}")
    def wait_url_to_be(self, url, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Дождаться URL, содержащего '{part}'")
    def wait_url_contains(self, part, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(part))

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        element = self.wait_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def type(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.wait_visible(locator).text.strip()

    def find(self, locator):
        return self.wait_visible(locator)

    def find_all(self, locator):
        WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            self.wait_visible(locator, timeout)
            return True
        except Exception:
            return False

    @allure.step("Прокрутить к элементу {locator}")
    def scroll_to(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_and_drop(self, source, target):
        self.driver.execute_script(_HTML5_DND_SCRIPT, source, target)

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url

    # --- Навигация по шапке ---
    @allure.step("Кликнуть «Конструктор» в шапке")
    def click_constructor(self):
        self.click(self.CONSTRUCTOR_LINK)

    @allure.step("Кликнуть «Лента Заказов» в шапке")
    def click_order_feed(self):
        self.click(self.ORDER_FEED_LINK)

    @allure.step("Кликнуть «Личный Кабинет» в шапке")
    def click_personal_account(self):
        self.click(self.PERSONAL_ACCOUNT_LINK)
