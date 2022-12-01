from django.db import models
from users.models import User


class RequestData(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    path = models.CharField(max_length=255)
    user = models.ForeignKey(User,
                             related_name='+',
                             on_delete=models.SET_NULL,
                             default=None, blank=True, null=True
                             )
    session_key = models.CharField(max_length=255)
    count_of_visits = models.PositiveSmallIntegerField()
    last_visit_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.path} - {self.user} - {self.session_key}'
