import random
import secrets
import string
from random import randint
from collections.abc import Iterator
from typing import NamedTuple
from faker import Faker

fake = Faker()


class User(NamedTuple):
    login: str
    email: str
    password: str


def generate_password() -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(randint(8, 15)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password


def generate_login(name: list) -> str:
    fake_name = name
    additional_part = [secrets.randbelow(100), random.randint(1960, 2022), f'{secrets.choice(string.ascii_letters)}']
    name_1 = [fake_name[0], fake_name[1]]
    name_2 = [fake_name[0], fake_name[1], '']
    separator = ['_', '']

    main_part = f'{secrets.choice(name_1)}{secrets.choice(separator)}{secrets.choice(name_2)}'
    return f'{main_part}{secrets.choice(separator)}{secrets.choice(additional_part)}'


def generate_email(name: list):
    return f'{generate_login(name).lower()}@mail.com'


def generate_users_data(amount: int) -> Iterator[User]:
    logins, emails, passwords = [], [], []
    while len(logins) != amount:
        name = fake.name().split()
        login = generate_login(name)
        email = generate_email(name)
        password = generate_password()
        if (login not in logins) and (email not in emails) and (password not in passwords):
            logins.append(login)
            emails.append(email)
            passwords.append(password)
            yield User(login=login, email=email, password=password)
