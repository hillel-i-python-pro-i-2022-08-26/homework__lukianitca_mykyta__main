import logging
import random
from typing import Iterator, Protocol, TypeAlias, NamedTuple

from faker import Faker

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


class User(NamedTuple):
    login: T_LOGIN
    password: T_PASSWORD


def validate(users: list[UserProtocol], amount: int) -> None:
    logins = set(map(lambda user: user.login, users))
    if amount != (amount_of_logins := len(logins)):
        raise ValueError(f'Not enough of unique items. Required: "{amount}". Provided: "{amount_of_logins}"')


def generate_users(amount: int) -> Iterator[UserProtocol]:
    faker = Faker()
    unique_logins: set[T_LOGIN] = set()
    while len(unique_logins) < amount:
        login = f"{faker.user_name()}_{faker.last_name().lower()}{random.randint(0, 1001)}"
        if login in unique_logins:
            continue
        unique_logins.add(login)
        password = faker.password()
        yield User(login, password)


def main():
    amount = 1000
    users = list(generate_users(amount=amount))
    validate(users=users, amount=amount)


if __name__ == "__main__":
    main()
