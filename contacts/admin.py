from django.contrib import admin
from . import models

admin.site.register(models.Contact)
# admin.site.register(models.Group)


class ContactInline(admin.TabularInline):
    model = models.Contact


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (ContactInline, )
