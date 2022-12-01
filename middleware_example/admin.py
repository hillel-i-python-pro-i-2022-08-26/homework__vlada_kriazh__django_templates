from django.contrib import admin
from . import models

admin.site.register(models.RequestData)


class UserInline(admin.TabularInline):
    model = models.RequestData
