from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)

    group = models.ForeignKey(Group,
                              related_name='contacts',
                              on_delete=models.CASCADE,
                              default=None, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__
