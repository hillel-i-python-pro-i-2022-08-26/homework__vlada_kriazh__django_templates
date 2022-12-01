# Generated by Django 4.1.3 on 2022-11-30 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RequestData",
            fields=[
                (
                    "key",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("path", models.CharField(max_length=255)),
                ("session_key", models.CharField(max_length=255)),
                ("count_of_visits", models.PositiveSmallIntegerField()),
                ("last_visit_date", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
