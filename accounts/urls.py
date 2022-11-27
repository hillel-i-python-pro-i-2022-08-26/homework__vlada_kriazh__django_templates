from django.urls import path
from accounts import views
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    # path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True,
    #                                              authentication_form=UserRegistrationForm), name='login'),
    path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True,
                                                 template_name='users/login.html',
                                                 authentication_form=LoginForm
                                                 ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
