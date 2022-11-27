from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='hello'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', views.profile, name='profile'),
    # path('accounts/register/', views.profile, name='register'),
    ]
