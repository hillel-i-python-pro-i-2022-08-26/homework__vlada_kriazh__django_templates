# Generated by Django 4.1.3 on 2022-11-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("middleware_example", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="requestdata",
            name="last_visit_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]