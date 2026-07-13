BASE_URL = "https://qa-stellarburgers.education-services.ru"

# UI-страницы
MAIN_PAGE = f"{BASE_URL}/"
LOGIN_PAGE = f"{BASE_URL}/login"
REGISTER_PAGE = f"{BASE_URL}/register"
FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"
FEED_PAGE = f"{BASE_URL}/feed"
ACCOUNT_PAGE = f"{BASE_URL}/account"
PROFILE_PAGE = f"{BASE_URL}/account/profile"
ORDER_HISTORY_PAGE = f"{BASE_URL}/account/order-history"

# API-эндпоинты (используются для подготовки данных: регистрация, создание заказа)
API_URL = f"{BASE_URL}/api"
REGISTER_API = f"{API_URL}/auth/register"
LOGIN_API = f"{API_URL}/auth/login"
USER_API = f"{API_URL}/auth/user"
INGREDIENTS_API = f"{API_URL}/ingredients"
ORDERS_API = f"{API_URL}/orders"
