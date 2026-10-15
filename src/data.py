from faker import Faker

fake = Faker()


class User:
    """Фабрика тестовых пользователей."""

    @staticmethod
    def random():
        return {
            "name": fake.first_name(),
            "email": fake.unique.email(),
            "password": fake.password(length=10),
        }
