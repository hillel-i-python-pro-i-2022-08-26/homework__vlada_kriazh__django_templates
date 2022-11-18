import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


def validate_phone(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError(
            _('%(value)s is not a valid number'),
            params={'value': value},
        )


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


def get_icon_path(instance, filename) -> str:
    _, extension = filename.rsplit('.', maxsplit=1)
    return f'contacts/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, validators=[validate_phone])
    date_of_birth = models.DateField()
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)

    group = models.ForeignKey(Group,
                              related_name='contacts',
                              on_delete=models.CASCADE,
                              default=None, blank=True, null=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to=get_icon_path
    )

    def get_absolute_url(self):
        return reverse('contacts:contact_edit', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
