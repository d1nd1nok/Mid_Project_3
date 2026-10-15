import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from src.data import User
from src.api_helpers import ApiClient
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from locators.constructor_page_locators import ConstructorPageLocators


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="all",
        choices=["chrome", "firefox", "all"],
        help="Браузер для запуска тестов: chrome, firefox или all (по умолчанию оба)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запускать браузер в headless-режиме",
    )


def _selected_browsers(config):
    choice = config.getoption("--browser")
    return ["chrome", "firefox"] if choice == "all" else [choice]


def pytest_generate_tests(metafunc):
    # Каждый тест, использующий фикстуру driver, прогоняется в выбранных браузерах
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", _selected_browsers(metafunc.config))


@pytest.fixture
def driver(request, browser):
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1080")
        web_driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=options)
        web_driver.set_window_size(1440, 1080)

    yield web_driver
    web_driver.quit()


@pytest.fixture
def registered_user():
    user = User.random()
    tokens = ApiClient.register_user(user)
    user["access_token"] = tokens["access_token"]
    yield user
    ApiClient.delete_user(user.get("access_token"))


@pytest.fixture
def ingredients():
    return ApiClient.get_ingredient_hashes()


@pytest.fixture
def logged_in_driver(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(registered_user["email"], registered_user["password"])
    ConstructorPage(driver).wait_visible(ConstructorPageLocators.PAGE_TITLE)
    return driver
