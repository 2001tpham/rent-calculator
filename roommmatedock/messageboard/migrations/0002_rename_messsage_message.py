# Generated by Django 4.1.7 on 2023-03-18 03:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentsplit', '0003_alter_expense_amount'),
        ('messageboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messsage',
            new_name='Message',
        ),
    ]
