from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)
