from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class MyUser(UserAdmin):
    add_form = UserRegistrationForm
    form = UserRegistrationForm
    model = get_user_model()
    list_display = ['email', 'password']


admin.site.register(models.User, UserAdmin)
