# Generated by Django 4.1.3 on 2022-11-29 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
