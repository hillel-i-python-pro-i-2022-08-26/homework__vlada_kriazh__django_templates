from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .services import generating


# @use_args({'amount': fields.Int()}, location="query")
# noinspection PyUnusedLocal
def print_users(request: HttpRequest, amount: int) -> HttpResponse:
    return render(
        request,
        'users.html',
        {
            'users': generating.generate_users_data(amount)
        }
    )
