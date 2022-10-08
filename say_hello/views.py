from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from webargs.djangoparser import use_args
from webargs import fields
from faker import Faker

faker = Faker()


def get_random_name() -> str:
    return faker.first_name()


@use_args({'name': fields.Str()}, location="query")
# noinspection PyUnusedLocal
def hello(request: HttpRequest, args) -> HttpResponse:
    if args.get('name') is None:
        name = get_random_name()
    else:
        name = args['name']
    return render(
        request,
        'hello.html',
        {
            'text': f'Hello, {name}!'
        }
    )
