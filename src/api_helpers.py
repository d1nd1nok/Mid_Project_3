import allure
import requests

from src.urls import REGISTER_API, USER_API, INGREDIENTS_API, ORDERS_API


class ApiClient:
    """
    Вспомогательный API-клиент.

    UI-тестам он нужен только для подготовки данных: быстро зарегистрировать
    пользователя, создать заказ и удалить пользователя после теста, не гоняя
    эти шаги через браузер.
    """

    @staticmethod
    @allure.step("API: зарегистрировать пользователя")
    def register_user(user):
        response = requests.post(REGISTER_API, data=user)
        assert response.status_code == 200, (
            f"Не удалось зарегистрировать пользователя: "
            f"{response.status_code} {response.text}"
        )
        body = response.json()
        return {
            "access_token": body["accessToken"],
            "refresh_token": body["refreshToken"],
        }

    @staticmethod
    @allure.step("API: удалить пользователя")
    def delete_user(access_token):
        if not access_token:
            return
        requests.delete(USER_API, headers={"Authorization": access_token})

    @staticmethod
    @allure.step("API: получить хэши ингредиентов")
    def get_ingredient_hashes(count=2):
        response = requests.get(INGREDIENTS_API)
        response.raise_for_status()
        data = response.json()["data"]
        return [item["_id"] for item in data[:count]]

    @staticmethod
    @allure.step("API: создать заказ")
    def create_order(access_token, ingredients=None):
        if ingredients is None:
            ingredients = ApiClient.get_ingredient_hashes()
        response = requests.post(
            ORDERS_API,
            headers={"Authorization": access_token},
            data={"ingredients": ingredients},
        )
        assert response.status_code == 200, (
            f"Не удалось создать заказ: {response.status_code} {response.text}"
        )
        return response.json()["order"]["number"]
