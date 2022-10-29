from django.urls import path
from get_sessions_info import views

app_name = 'sessions'

urlpatterns = [
    path('', views.get_session, name='index'),
]
