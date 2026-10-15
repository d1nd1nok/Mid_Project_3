# Diplom_3

Третья часть дипломного проекта курса «Инженер по тестированию» (Яндекс Практикум): UI-автотесты для веб-приложения [Stellar Burgers](https://qa-stellarburgers.education-services.ru/) на Selenium с Page Object Model, кроссбраузерным запуском в Google Chrome и Mozilla Firefox и Allure-отчётом.

## Стек

- Python 3
- pytest
- Selenium WebDriver — Google Chrome и Mozilla Firefox (драйверы подтягивает Selenium Manager)
- requests — подготовка данных через API
- Faker — генерация тестовых пользователей
- Allure (`allure-pytest`)

## Структура проекта

```
Diplom_3/
├── conftest.py            # фикстуры: driver (Chrome / Firefox), registered_user, logged_in_driver, ingredients
├── pytest.ini             # настройки pytest: pythonpath и --alluredir
├── requirements.txt       # зависимости
├── locators/              # локаторы — отдельный класс на каждую страницу
├── pages/                 # Page Object
│   ├── base_page.py             # BasePage — общие методы: клики, ввод, ожидания, навигация в шапке
│   ├── login_page.py            # LoginPage — вход
│   ├── forgot_password_page.py  # ForgotPasswordPage — восстановление пароля
│   ├── reset_password_page.py   # ResetPasswordPage — ввод нового пароля
│   ├── account_page.py          # AccountPage — личный кабинет и история заказов
│   ├── constructor_page.py      # ConstructorPage — конструктор бургеров
│   └── feed_page.py             # FeedPage — лента заказов
├── src/
│   ├── urls.py            # URL страниц и API-эндпоинтов
│   ├── data.py            # User — фабрика тестовых пользователей
│   └── api_helpers.py     # ApiClient — регистрация, удаление пользователя и создание заказа через API
├── tests/
│   ├── test_forgot_password.py  # TestForgotPassword — восстановление пароля
│   ├── test_account.py          # TestAccount — личный кабинет
│   ├── test_constructor.py      # TestConstructor — основной функционал
│   └── test_feed.py             # TestFeed — лента заказов
└── allure-results/        # результаты прогона для Allure-отчёта
```

Пользователей и заказы для тестов создаёт API (`ApiClient`), чтобы не гонять подготовительные шаги через браузер. После теста пользователь удаляется.

## Тесты

| Класс | Тест | Что проверяет |
|-------|------|---------------|
| `TestForgotPassword` | `test_open_forgot_password_page` | Переход на страницу восстановления по кнопке «Восстановить пароль» |
| | `test_submit_email_opens_reset_page` | Ввод почты и клик по «Восстановить» открывают страницу ввода нового пароля |
| | `test_show_hide_password_highlights_field` | Клик по кнопке показать/скрыть пароль подсвечивает поле |
| `TestAccount` | `test_open_personal_account` | Переход по клику на «Личный Кабинет» |
| | `test_open_order_history` | Переход в раздел «История заказов» |
| | `test_logout` | Выход из аккаунта |
| `TestConstructor` | `test_go_to_constructor` | Переход по клику на «Конструктор» |
| | `test_go_to_order_feed` | Переход по клику на «Лента Заказов» |
| | `test_ingredient_modal_opens` | Клик по ингредиенту открывает окно с деталями |
| | `test_ingredient_modal_closes` | Окно ингредиента закрывается по крестику |
| | `test_ingredient_counter_increases` | При добавлении ингредиента в заказ растёт его счётчик |
| | `test_logged_in_user_can_place_order` | Залогиненный пользователь может оформить заказ |
| `TestFeed` | `test_order_modal_opens` | Клик по заказу открывает окно с деталями |
| | `test_user_order_appears_in_feed` | Заказы из «Истории заказов» отображаются в «Ленте заказов» |
| | `test_total_counter_increases` | Новый заказ увеличивает счётчик «Выполнено за всё время» |
| | `test_today_counter_increases` | Новый заказ увеличивает счётчик «Выполнено за сегодня» |
| | `test_new_order_appears_in_progress` | Номер нового заказа появляется в разделе «В работе» |

Каждый тест прогоняется в обоих браузерах: параметр `browser` подставляется в `conftest.py` через `pytest_generate_tests`.

## Запуск

1. Установите Google Chrome и Mozilla Firefox.
2. Создайте виртуальное окружение и установите зависимости:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Запустите тесты. Результаты для Allure сохраняются в `allure-results` автоматически (настроено в `pytest.ini`):

   ```bash
   # в обоих браузерах (по умолчанию)
   pytest tests

   # только в одном браузере
   pytest tests --browser=chrome
   pytest tests --browser=firefox

   # без открытия окна браузера
   pytest tests --headless
   ```

4. Откройте отчёт (нужен установленный [Allure CLI](https://allurereport.org/docs/install/)):

   ```bash
   allure serve allure-results
   ```

---

## Задание

Протестируй веб-приложение Stellar Burgers.

### Что нужно сделать

1. Опиши элементы, которые будешь использовать в тестах, с помощью паттерна Page Object Model.
2. Протестируй функциональность в Google Chrome и Mozilla Firefox.
3. Подключи Allure-отчёт.

### Восстановление пароля

Проверь:

- переход на страницу восстановления пароля по кнопке «Восстановить пароль»;
- ввод почты и клик по кнопке «Восстановить»;
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.

### Личный кабинет

Проверь:

- переход по клику на «Личный кабинет»;
- переход в раздел «История заказов»;
- выход из аккаунта.

### Основной функционал

Проверь:

- переход по клику на «Конструктор»;
- переход по клику на «Лента заказов»;
- если кликнуть на ингредиент, появится всплывающее окно с деталями;
- всплывающее окно закрывается кликом по крестику;
- при добавлении ингредиента в заказ увеличивается каунтер этого ингредиента;
- залогиненный пользователь может оформить заказ.

### Раздел «Лента заказов»

Проверь:

- если кликнуть на заказ, откроется всплывающее окно с деталями;
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»;
- при создании нового заказа счётчик «Выполнено за всё время» увеличивается;
- при создании нового заказа счётчик «Выполнено за сегодня» увеличивается;
- после оформления заказа его номер появляется в разделе «В работе».
