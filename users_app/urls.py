from django.urls import path
from . import views

app_name = 'users_generator'

urlpatterns = [
    # path('', views.index, name='hello'),
    path('<int:amount>', views.print_users, name='index')
]
