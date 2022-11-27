from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    # return render(request, 'base.html')
    return render(
        request,
        'main.html',
        {'request': request}
    )


# def profile(request: HttpRequest) -> HttpResponse:
#     return render(
#         request,
#         'registration/profile.html',
#         {'request': request}
#     )
