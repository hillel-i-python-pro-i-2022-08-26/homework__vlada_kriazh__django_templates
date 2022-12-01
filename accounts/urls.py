from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    # path('login/', views.CustomLoginView.as_view(redirect_authenticated_user=True,
    #                                              authentication_form=UserRegistrationForm), name='login'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                template_name='users/login.html',
                                                ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<int:pk>/edit/', views.UserUpdateView.as_view(), name='profile_edit')
]
