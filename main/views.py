from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_project2.settings import INIT_INFO_MIDDLEWARE


def index(request: HttpRequest) -> HttpResponse:

    return render(
        request,
        'base.html',
        {'request': request}
    )


# def profile(request: HttpRequest) -> HttpResponse:
#     return render(
#         request,
#         'registration/profile.html',
#         {'request': request}
#     )
