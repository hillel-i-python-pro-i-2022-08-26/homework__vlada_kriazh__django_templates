from django.urls import path
from . import views

app_name = 'say_hello'

urlpatterns = [
    path('', views.hello, name='index')
]
