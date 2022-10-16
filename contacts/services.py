import random
from collections.abc import Iterator
from faker import Faker
from contacts import models
from datetime import datetime as DT
from datetime import timedelta

faker = Faker()


def generate_name():
    name = faker.name()
    return name


def generate_phone():
    prefix = ['039', '067', '068', '096', '097', '098', '050', '066', '095', '099', '063', '073', '093', '091']
    number = random.choice(prefix)
    for _ in range(7):
        number += str(random.randint(0, 9))
    return number


def generate_date():
    start = DT.strptime('01.01.1942', '%d.%m.%Y')
    end = DT.strptime('01.01.2012', '%d.%m.%Y')
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))


def generate_contacts(amount: int) -> Iterator[models.Contact]:
    names = set()
    phones = set()

    while len(names) < amount:
        name = generate_name()
        phone = generate_phone()

        if name in names:
            continue
        if phone in phones:
            continue

        names.add(name)
        phones.add(phone)
        yield models.Contact(
            name=name,
            phone=phone,
            date_of_birth=generate_date(),
        )
