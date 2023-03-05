# Generated by Django 4.1.7 on 2023-03-03 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentsplit', '0004_expense_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_fr_profile', to='rentsplit.profileauth'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_fr_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
