from django.contrib import admin
from . import models


# class MyUser(UserAdmin):
#     add_form = UserRegistrationForm
#     form = UserRegistrationForm
#     model = get_user_model()
#     list_display = ['email', 'password']
#
#
# admin.site.register(models.User, UserAdmin)


admin.site.register(models.User)


class ContactInline(admin.TabularInline):
    model = models.User
